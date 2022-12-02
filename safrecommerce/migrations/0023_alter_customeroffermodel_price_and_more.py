# Generated by Django 4.1.3 on 2022-12-02 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safrecommerce', '0022_customeroffermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeroffermodel',
            name='price',
            field=models.DecimalField(decimal_places=2, default=150.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='customeroffermodel',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=4.0, max_digits=5),
        ),
    ]
