from django.views.generic import ListView
from django.shortcuts import render
from .models import *

# Create your views here.
# class SaffronHomePageListView(ListView):
#     model = SaffronProducts
#     template_name = "SaffronECommerce/index.html"

def index(request):
    products = SaffronProducts.objects.all()
    info_blocks = SaffroonBGInfo.objects.all()
    commercial_pars = CommercialOfferParameeters.objects.all()
    contact_info = ContactInfo.objects.all()
    
    return render(
        request,
        './safrecommerce/index.html',
        {'products':products,'info_blocks':info_blocks, 'commercial_pars':commercial_pars,"contact_info":contact_info }
        )