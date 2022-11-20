# Generated by Django 4.1.3 on 2022-11-20 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safrecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='safrapp',
            options={'verbose_name': "Saffron's product", 'verbose_name_plural': "Saffron's products"},
        ),
        migrations.AddField(
            model_name='safrapp',
            name='price',
            field=models.DecimalField(decimal_places=2, default=500.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='safrapp',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=4.0, max_digits=5),
        ),
    ]