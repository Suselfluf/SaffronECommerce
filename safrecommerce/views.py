from django.views.generic import ListView
from django.shortcuts import render

from .forms import CustomerOfferForm
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
    form = CustomerOfferForm()
    if request.method == "POST":
        form = CustomerOfferForm(request.POST)
        print("Printing post:", request.POST)
        # if form.is_valid():
        #     form.save()
       
    return render(
        request,
        './safrecommerce/index.html',
        {'products':products,'info_blocks':info_blocks, 'commercial_pars':commercial_pars,"contact_info":contact_info, 'form':form}
        )