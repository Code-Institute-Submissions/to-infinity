# Generated by Django 3.1.4 on 2020-12-10 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0009_destination_addons'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_ref', models.CharField(editable=False, max_length=32)),
                ('booking_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stripe_pid', models.CharField(default='0', max_length=254)),
                ('status', models.CharField(choices=[('INITIAL', 'Initial'), ('RESERVED', 'Reserved'), ('COMPLETE', 'Complete')], default='INITIAL', max_length=10)),
                ('lead_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('seats_available', models.IntegerField(editable=False)),
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
                ('is_leaduser', models.BooleanField(default=False)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passengers', to='bookings.booking')),
                ('trip_addons', models.ManyToManyField(to='products.AddOn')),
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
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookings.trip'),
        ),
    ]
