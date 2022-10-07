from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import extendeduser,State,City,Category,subcat,Product,prverification
import datetime
from django.conf import settings
# Create your views here.

def homepage(request):
    if request.method=='POST':
        subcaty = request.POST['subcat']
        pgobjs = Product.objects.filter(subcatname = subcaty,verifystatus = True).order_by('price')
        subcats = subcat.objects.all()
        return render(request,'homepage.html',{'pgobjs' : pgobjs, 'subcats' : subcats})
    else :
        pgobjs = Product.objects.filter(verifystatus = True,activestatus=True).order_by('price')
        subcats = subcat.objects.all()
        return render(request,'homepage.html',{'pgobjs' : pgobjs, 'subcats' : subcats})

def register(request):
    if request.method == 'POST':
        #variablename=request.POST['html_variable_name']
        username = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['phone']
        password1 = request.POST['password']
        password2 = request.POST['retypepassword']

        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=email,email=email,password=password1,first_name=username)
                newextendeduser = extendeduser(mobile=mobile, user=user)
                newextendeduser.save();
                messages.info(request,'user created')
                return redirect('login')
                
        else:      
            messages.info(request,'passwords not matching')
            return redirect('register')
 
    else:
        return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                messages.info(request,'Login Successful')
                return redirect("/emphome")
            else:    
                auth.login(request, user)
                messages.info(request,'Login Successful')
                return redirect("/")
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def forresellers(request):
    return render(request,'forresellers.html')    

def addnewproduct(request):
    if request.method == 'POST':
        userid = request.user.id
        prname = request.POST['prname']
        img = request.FILES['img']
        statenamee = request.POST['statename']
        citynamee = request.POST['cityname']
        catnamee = request.POST['catname']
        subcatnamee = request.POST['subcatname']
        brandname = request.POST['brandname']
        yop = request.POST['yop']
        praddress = request.POST['praddress']
        desc = request.POST['descriptions']
        price = request.POST['price']
        bankname = request.POST['bankname']
        accountno = request.POST['accountno']
        ifsccode = request.POST['ifsccode']
        st = State.objects.get(id=statenamee)
        statename1 = st.statename
        ct = City.objects.get(id=citynamee)
        cityname1 = ct.cityname
        cat = Category.objects.get(id=catnamee)
        catname1 = cat.catname
        sub = subcat.objects.get(id=subcatnamee)
        subcatname1 = sub.subcatname
        payment = 50
        userid = request.user.id

        newproduct = Product(userid_id=userid,prname=prname,catname_id=catnamee,subcatname_id=subcatnamee,catname1=catname1,subcat1=subcatname1,img=img,statename_id=statenamee,cityname_id=citynamee,statename1=statename1,cityname1=cityname1,brandname=brandname,yop=yop,bankname=bankname,accountno=accountno,ifsccode=ifsccode,praddress=praddress,desc=desc,price=price,payment=payment)
        newproduct.save();
        messages.info(request,'New Product Added Successfully')
        return render(request,'forresellers.html',)
    
    else:
        stateobj= State.objects.all()
        cityobj= City.objects.all()
        catobj= Category.objects.all()
        subobj= subcat.objects.all()
        return render(request,'addnewproduct.html',{'States':stateobj,'Cities':cityobj,'cats':catobj,'subcats':subobj})

def yourprlist(request):
    userid = request.user.id
    probj = Product.objects.filter(userid=userid)
    return render(request,'yourprlist.html',{'probj' : probj})

# def editlisting(request):
#     if request.method == 'POST':
#         if 'edit' in request.POST:
#             prid = request.POST['prid']
#             prname = request.POST['prname']
#             brandname = request.POST['brandname']
#             price = request.POST['price']
#             desc = request.POST['descriptions']
#             activestatus = request.POST['activestatus']

#             editroom = Product.objects.get(id = roomid)
#             editroom.pgname = pgname
#             editroom.price = price
#             editroom.desc=desc
#             editroom.bedno=bedno
#             editroom.availbalebed = bedno
#             editroom.freebed = bedno
#             editroom.activestatus = activestatus
#             editroom.save();
#             messages.info(request,'Update successful')
#             return render(request,'yourpglist.html',)
            
#     else:    
#         id = request.GET.get('pg')
#         roomobj = Product.objects.filter(id=id)
#         return render(request,'editlisting.html',{'roomobj' : roomobj})

def emphome(request):   
    if request.user.is_staff:
        probj = Product.objects.filter(verifystatus=False)  
        return render(request,'emphome.html',{'probj' : probj})
    else:
        return render(request,"homepage.html")       

def acceptrequest(request):
    pr_id = request.GET.get('pg') 
    pr = Product.objects.get(id=pr_id)
    myuserid = pr.userid_id
    usermobobj = extendeduser.objects.get(user=myuserid)
    commitobj = prverification.objects.filter(prid=pr_id,allotedstatus=True).first()
    return render(request,'acceptrequest.html',{'pr' : pr, 'usermobobj' : usermobobj, 'commitobj' : commitobj})

def commiting(request):
    prid = request.GET.get('pg')
    verifier = request.user.id
    commit = prverification(allotedstatus=True,prid_id=prid,verifier_id=verifier)
    commit.save();
    messages.info(request,'You can now verify the alloted slot')
    return redirect('emphome') 

def verification(request):
    userid = request.user.id
    prverifyobj = prverification.objects.filter(allotedstatus=True,verifier_id=userid)
    
    return render(request,'verification.html',{'prverifyobj' : prverifyobj})  

def unallot(request):
    verifyid = request.GET.get('pg')
    allotedlot = prverification.objects.get(id = verifyid)
    allotedlot.allotedstatus = False
    allotedlot.save();
    messages.info(request,'Slot Unallocation done successfully!!!')
    return redirect('verification')

def verifing(request):
    if request.method == 'POST':
        verifyid = request.POST['verifyid']
        pgname = request.POST['pgname']
        brandname = request.POST['bname']
        pgroomid = request.POST['pgroomid']
        addescription = request.POST['description']
        pgaddress = request.POST['pgaddress']
        adprice = request.POST['price']
        yop = request.POST['yop']
        bankname = request.POST['bankname']
        accountno = request.POST['accountno']
        ifsccode = request.POST['ifsccode']
        verifyfeedback = request.POST['feedback']


        roomobj = Product.objects.get(id = pgroomid)
        roomobj.verifystatus = True
        roomobj.pgname = pgname
        roomobj.brandname = brandname
        roomobj.desc = addescription
        roomobj.pgaddress = pgaddress
        roomobj.price = adprice
        roomobj.yop = yop
        roomobj.bankname = bankname
        roomobj.accountno = accountno
        roomobj.ifsccode = ifsccode
        
        verifyobj = prverification.objects.get(id = verifyid)
        verifyobj.feedback = verifyfeedback
        verifyobj.verifydate = datetime.datetime.now()

        roomobj.save();
        verifyobj.save();
        messages.info(request,'Slot verified successfully!!!')
        return redirect('verifiedbyme')        


    else:
        verifyid = request.GET.get('verify')
        roomid = request.GET.get('room')
        verifyobjs = prverification.objects.get(id = verifyid)
        roomobjs = Product.objects.get(id = roomid)
        return render(request,'verifing.html',{'verifyobjs' : verifyobjs, 'roomobjs' : roomobjs})

def verifiedbyme(request):
    userid = request.user.id
    pgverifyobj = prverification.objects.filter(verifier_id=userid,prid__verifystatus=True,allotedstatus=True)  
    return render(request,'verifiedbyme.html',{'pgverifyobj' : pgverifyobj})

def proverview(request):
    if request.user.is_authenticated:
    #     if request.method == 'POST':
    #         bookingtime = datetime.datetime.now()
    #         roomid = request.POST['roomid']
    #         userid = request.user.id
    #         payment = request.
            # stripe.api_key = settings.STRIPE_SECRET_KEY
        
            # stripe_total = 100000
            # userid = request.user.id

            # token = request.POST['stripeToken']
            # email = request.POST['stripeEmail']
            # customer = stripe.Customer.create(email=email,source=token)
            # charge = stripe.Charge.create(amount=stripe_total,currency="inr",customer=customer.id)

            # bookingobj = booking(booktime=bookingtime,prid_id=roomid,userid_id=userid,payment=payment,paymentstatus=True)
            # bookingobj.save();

            # loteditobj = Room.objects.get(id=roomid)
            # loteditobj.save();
            # messages.info(request,'Succesfully Booked')
            # return redirect('/')           

        # else:   
        #     stripe.api_key = settings.STRIPE_SECRET_KEY
        #     data_key = settings.STRIPE_PUBLISHABLE_KEY
        #     stripe_total = 100000                
             room = request.GET.get('pg')
             pgobjs = Product.objects.get(id=room)  
             myuserid = pgobjs.userid_id
             usermobobj = extendeduser.objects.get(user=myuserid)
             return render(request,'proverview.html',{'pgobjs' : pgobjs,'usermobobj' : usermobobj})
    else:
        messages.info(request,'Please Login to Continue')
        return redirect('login') 

