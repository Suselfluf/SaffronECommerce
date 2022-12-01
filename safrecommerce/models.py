from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class SaffronProducts(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=500.00)
    weightInGr = models.DecimalField(max_digits=10, decimal_places=2, default=4.00)
    weightInSot = models.IntegerField()
    image = models.ImageField(upload_to='images/', max_length=None)
    
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.title

class SaffroonBGInfo(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None, blank=True)
    
    class Meta:
        verbose_name = ("Block with information")
        verbose_name_plural = ("Blocks with information")

    def __str__(self):
        return self.title
    
    
class CommercialOfferParameeters(models.Model):
    
    title = models.CharField(max_length=100, default="1st Commercial Offer")
    minimalBulkWeight = models.DecimalField(max_digits=10, default=100.00, decimal_places=2)
    wholesalePriceForGram = models.DecimalField(max_digits=10, decimal_places=2, default=150.00)
    retailPriceForGram = models.DecimalField(max_digits=10, decimal_places=2, default=200.00)

    class Meta:
        verbose_name = ("Commercial offer")
        verbose_name_plural = ("Commercial offers")

    def __str__(self):
        return self.title 
    
    
    
class CustomerOfferModel(models.Model):
    
    email = models.EmailField(max_length=254)           ##Make this field required to fill in form
    description = models.TextField(max_length=400, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=4.00)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=4.00) 
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Offer created at:")
    class Meta:
        verbose_name = ("Customer's offer")
        verbose_name_plural = ("Customers's offers")

    def __str__(self):
        return self.email   

    
class ContactInfo(models.Model):
    
    name = models.CharField(max_length=50, default="Ethan Shagaei")
    telegramm = models.CharField(max_length=50, default="@EthanShagaei")
    phoneNumber = PhoneNumberField(null=False, blank=True, unique=True)
    class Meta:
        verbose_name = ("Contacts Data")
        verbose_name_plural = ("Contacts Data")

    def __str__(self):
        return self.name   
