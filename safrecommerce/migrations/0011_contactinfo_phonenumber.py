# Generated by Django 4.1.3 on 2022-11-24 12:36

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('safrecommerce', '0010_commercialofferparameeters_contactinfo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='phoneNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True),
        ),
    ]
