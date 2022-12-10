from django.forms import ModelForm
from .models import *

class CustomerOfferForm(ModelForm):
    class Meta:
        model = CustomerOfferModel
        fields = ['email', 'name', 'phoneNumber', 'description', 'weight', 'price']
        
        
        
    # email = models.EmailField(max_length=254)           ##Make this field required to fill in form
    # description = models.TextField(max_length=400, blank=True)
    # weight = models.DecimalField(max_digits=5, decimal_places=2, default=4.00)
    # price = models.DecimalField(max_digits=10, decimal_places=2, default=4.00) 
    
    
    # https://www.youtube.com/watch?v=EX6Tt-ZW0so