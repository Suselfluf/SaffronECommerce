# Generated by Django 4.1.3 on 2022-12-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safrecommerce', '0024_alter_customeroffermodel_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='commercialofferparameeters',
            name='minumalOfferWeight',
            field=models.DecimalField(decimal_places=1, default=1.0, max_digits=10),
        ),
    ]
