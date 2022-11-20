
from django.contrib import admin
from .models import SafrApp

# Register your models here.
class SaffrAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image', 'price', 'weight')
    list_display_links = ('id', 'title')
    search_fields = ('id','title','description')
    list_editable = ('price','weight')
    list_filter = ('price','weight')
    
admin.site.register(SafrApp, SaffrAdmin)