from django.db import models

# Create your models here.
class SaffronProducts(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=500.00)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=4.00)
    image = models.ImageField(upload_to='./SaffronECommerce/static/images/', height_field=None, width_field=None, max_length=None)
    

    class Meta:
        verbose_name = ("Saffron's Product")
        verbose_name_plural = ("Saffron's Products")

    def __str__(self):
        return self.title

class SaffroonBGInfo(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=800, blank=True)
    image = models.ImageField(upload_to='./SaffronECommerce/static/images/', height_field=None, width_field=None, max_length=None, blank=True)
    
    class Meta:
        verbose_name = ("Saffron's History")
        verbose_name_plural = ("Saffrons's History")

    def __str__(self):
        return self.title
    
    
class CommercialOfferParameeters(models.Model):
    
    title = models.CharField(max_length=100, default="1st Commercial Offer")
    minimalBulkWeight = models.DecimalField(max_digits=7, default=100.00, decimal_places=2)
    wholesalePriceForGram = models.DecimalField(max_digits=7, decimal_places=2, default=150.00)
    retailPriceForGram = models.DecimalField(max_digits=7, decimal_places=2, default=150.00)

    class Meta:
        verbose_name = ("Commercial offer parameters administration")
        verbose_name_plural = ("Commercial offer parameters administration")

    def __str__(self):
        return self.title 
    
    
    
class CustomerOfferModel(models.Model):
    
    email = models.EmailField(max_length=254)           ##Make this field required to fill in form
    description = models.TextField(max_length=400, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=4.00)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=4.00) 
    
    class Meta:
        verbose_name = ("Saffron's History")
        verbose_name_plural = ("Saffrons's History")

    def __str__(self):
        return self.title   

    
class ContactInfo(models.Model):
    
    telegramm = models.CharField(max_length=50, default="@EthanShagaei")
    # phonenumber = models.PhoneNumberField(blank=True)
    class Meta:
        verbose_name = ("Saffron's History")
        verbose_name_plural = ("Saffrons's History")

    def __str__(self):
        return self.title   
