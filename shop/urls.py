from django.urls import path
from . import views
urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("logout/",views.logout,name="logout"),
    path("forresellers",views.forresellers,name="forresellers"),
    path("addnewproduct",views.addnewproduct,name="addnewproduct"),
    path("yourprlist",views.yourprlist,name="yourprlist"),
    path("emphome",views.emphome,name="emphome"),
    path('acceptrequest/',views.acceptrequest, name='acceptlisting'),
    path('commiting/',views.commiting, name='commiting'),
    path('verification',views.verification, name='verification'),
    path('unallot/',views.unallot, name='unallot'),
    path('verifing/',views.verifing, name='verifing'),
    path('verifing',views.verifing, name='verifing'),
    path('verifiedbyme',views.verifiedbyme, name='verifiedbyme'),
    path('proverview/',views.proverview, name='proverview'),
    path('proverview',views.proverview, name='proverview'),
]