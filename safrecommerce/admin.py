
from django.contrib import admin
from .models import *

# Register your models here.
class SaffrProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'price', 'weightInGr','weightInSot')
    list_display_links = ('id', 'title')
    search_fields = ('id','title','description')
    list_editable = ('price','weightInSot')
    list_filter = ('price','weightInSot')
    
class SaffrBGInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id','title',)
    # list_editable = ('title')
    list_filter = ('title',)
    
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','minimalBulkWeight','wholesalePriceForGram','retailPriceForGram')
    # list_display_links = ('id', 'title')
    search_fields = ('id','title',)
    list_editable = ('title','minimalBulkWeight','wholesalePriceForGram','retailPriceForGram')
    list_filter = ('wholesalePriceForGram','retailPriceForGram')

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'telegramm', 'phoneNumber')
    search_fields = ('id','name',)
    list_editable = ('name', 'telegramm', 'phoneNumber')
    list_filter = ('name',)
    
    
admin.site.register(SaffronProducts, SaffrProductsAdmin)
admin.site.register(SaffroonBGInfo, SaffrBGInfoAdmin)
admin.site.register(CommercialOfferParameeters, OfferAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)