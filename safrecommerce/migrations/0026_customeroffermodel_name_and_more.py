# Generated by Django 4.1.3 on 2022-12-10 20:02

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('safrecommerce', '0025_commercialofferparameeters_minumalofferweight'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeroffermodel',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='customeroffermodel',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True),
        ),
    ]
