# Generated by Django 4.1.3 on 2022-11-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safrecommerce', '0006_alter_saffroonbginfo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saffroonbginfo',
            name='image',
            field=models.ImageField(blank=True, upload_to='./SaffronECommerce/static/images/'),
        ),
    ]
