# Generated by Django 4.1.3 on 2022-11-26 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safrecommerce', '0017_alter_saffronproducts_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saffronproducts',
            name='image',
            field=models.ImageField(upload_to='./static/images/'),
        ),
    ]