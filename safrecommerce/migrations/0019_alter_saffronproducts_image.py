# Generated by Django 4.1.3 on 2022-11-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safrecommerce', '0018_alter_saffronproducts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saffronproducts',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
