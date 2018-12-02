from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name' ,'listing','email','contact_date','attended')
    list_display_links = ('id','name')
    search_fields = ('namne','email','listings')
    list_per_page = 25
    list_filter = ('attended',)
    list_editable = ('attended',)


admin.site.register(Contact,ContactAdmin)
