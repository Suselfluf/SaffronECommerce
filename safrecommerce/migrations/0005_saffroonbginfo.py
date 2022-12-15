# Generated by Django 4.1.3 on 2022-11-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safrecommerce', '0004_rename_safrapp_saffronproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaffroonBGInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, upload_to=None)),
            ],
            options={
                'verbose_name': "Saffron's History",
                'verbose_name_plural': "Saffrons's History",
            },
        ),
    ]
