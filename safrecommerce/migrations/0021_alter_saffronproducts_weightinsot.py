# Generated by Django 4.1.3 on 2022-11-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safrecommerce', '0020_rename_weight_saffronproducts_weightingr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saffronproducts',
            name='weightInSot',
            field=models.IntegerField(),
        ),
    ]
