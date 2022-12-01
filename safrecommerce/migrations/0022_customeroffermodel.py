# Generated by Django 4.1.3 on 2022-12-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safrecommerce', '0021_alter_saffronproducts_weightinsot'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOfferModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(blank=True, max_length=400)),
                ('weight', models.DecimalField(decimal_places=2, default=4.0, max_digits=5)),
                ('price', models.DecimalField(decimal_places=2, default=4.0, max_digits=10)),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Offer created at:')),
            ],
            options={
                'verbose_name': "Customer's offer",
                'verbose_name_plural': "Customers's offers",
            },
        ),
    ]