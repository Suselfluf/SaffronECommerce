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
        pDict = request.POST.copy()
        # print(",".join(request.POST.getlist('description')))
        form = CustomerOfferForm(pDict)
        print("Printing post:", pDict)
        if form.is_valid():                 # Unfortunately can not provide duplicating phonenumbers within the database, however can serve as protection from sending multiple same data request
            form.save()
            form = CustomerOfferForm()
            # form.clean()
        else:
            print("Wrong")
       
    return render(
        request,
        './safrecommerce/index.html',
        {'products':products,'info_blocks':info_blocks, 'commercial_pars':commercial_pars,"contact_info":contact_info, 'form':form}
        )