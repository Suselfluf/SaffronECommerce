
from django.contrib import admin
from .models import *

# Register your models here.
class SaffrProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'price', 'weight')
    list_display_links = ('id', 'title')
    search_fields = ('id','title','description')
    list_editable = ('price','weight')
    list_filter = ('price','weight')
    
class SaffrBGInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id','title',)
    # list_editable = ('title')
    list_filter = ('title',)
    
admin.site.register(SaffronProducts, SaffrProductsAdmin)
admin.site.register(SaffroonBGInfo, SaffrBGInfoAdmin)