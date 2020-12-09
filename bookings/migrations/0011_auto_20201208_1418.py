# Generated by Django 3.1.4 on 2020-12-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_destination_addons'),
        ('bookings', '0010_auto_20201206_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='passenger',
            name='trip_addons',
            field=models.ManyToManyField(to='products.AddOn'),
        ),
        migrations.AddField(
            model_name='passenger',
            name='trip_insurance',
            field=models.ManyToManyField(to='products.Insurance'),
        ),
    ]