# Generated by Django 3.1.4 on 2020-12-21 18:34

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_ref', models.CharField(editable=False, max_length=32)),
                ('booking_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(choices=[('INITIAL', 'Initial'), ('RESERVED', 'Reserved'), ('COMPLETE', 'Complete')], default='INITIAL', max_length=10)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('country', django_countries.fields.CountryField(default='', max_length=2)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('town_or_city', models.CharField(default='', max_length=40)),
                ('street_address1', models.CharField(default='', max_length=80)),
                ('street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('lead_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('seats_available', models.IntegerField(editable=False)),
                ('trip_ref', models.CharField(blank=True, max_length=32, null=True)),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trips', to='products.destination')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('passport_no', models.CharField(max_length=12)),
                ('is_leaduser', models.BooleanField(default=False)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passengers', to='bookings.booking')),
                ('trip_addons', models.ManyToManyField(blank=True, to='products.AddOn')),
                ('trip_insurance', models.ManyToManyField(to='products.Insurance')),
            ],
        ),
        migrations.CreateModel(
            name='BookingLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('line_total', models.DecimalField(decimal_places=2, editable=False, max_digits=8)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='bookings.booking')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='bookings.trip'),
        ),
    ]
