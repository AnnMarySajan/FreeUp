from django.contrib import admin
from django.contrib.admin import ModelAdmin,register

from .models import Product, State,City,extendeduser,Category,subcat
from django.db.models.aggregates import Avg,Sum
from django.db.models import Count,Avg
# Register your models here.

@register(State)
class StateAdmin(ModelAdmin):
    list_display = ('id','statename')

@register(City)
class CityAdmin(ModelAdmin):
    list_display = ('id','statename','cityname')

@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id','catname','catcommission')    

@register(subcat)
class subcatAdmin(ModelAdmin):
    list_display = ('id','catname','subcatname')      

@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('id','prname','get_name','get_userid','catname','subcatname','statename','cityname','price','verifystatus','activestatus')
    list_filter = ('statename','cityname','catname','subcatname','activestatus','verifystatus')
    def get_name(self, obj):
        return obj.userid.first_name
    get_name.admin_order_field  = 'userid'  #Allows column order sorting
    get_name.short_description = 'User Name'  #Renames column head
    def get_userid(self, obj):
        return obj.userid.id
    get_userid.short_description = 'User ID'    