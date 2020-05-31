from django.contrib import admin

from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    #Properties To Display In Admin Page
    list_display = (
        'id',
        'title',
        'is_published', 
        'price',
        'list_date',
        'realtor'
    )
    #Gives the ability to click on the property
    list_display_links = ('id','title')
    #Filtering ability
    list_filter = ('realtor',)
    #Allow Edit from the Admin Page
    list_editable = ('is_published',)
    #Create a search field
    search_fields = (
        'title',
        'description',
        'address',
        'city',
        'state',
        'zipcode',
        'price',
    )
    list_per_page = 25
    
admin.site.register(Listing,ListingAdmin)