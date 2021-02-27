from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'rent_price', 'buying_price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'locality', 'estate', 'rent_price','buying_price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
