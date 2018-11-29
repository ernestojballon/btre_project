from django.contrib import admin
from .models import Listing
from django.db import models
from realtors.models import Realtor


def realtor_number(obj):
    realtorPhone = Realtor.objects.get(name=obj.realtor).phone
    # realtor = obj.realtor.phone
    return realtorPhone

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor',realtor_number)
    list_display_links = ('id','title')
    list_filter = ('is_published','realtor')
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','state','zipcode','price' )
    list_per_page = 25
admin.site.register(Listing,ListingAdmin)
