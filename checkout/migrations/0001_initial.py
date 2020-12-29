# Generated by Django 3.1.4 on 2020-12-28 18:59

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('original_bag', models.TextField(default='')),
                ('stripe_pid', models.CharField(default='', max_length=254)),
            ],
        ),
    ]
