from django.db import models

# Create your models here.
class SafrApp(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=500.00)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=4.00)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    

    class Meta:
        verbose_name = ("Saffron's product")
        verbose_name_plural = ("Saffron's products")

    def __str__(self):
        return self.title

    
