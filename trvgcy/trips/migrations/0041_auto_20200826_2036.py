# Generated by Django 3.0.8 on 2020-08-26 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0040_auto_20200826_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triptemplate',
            name='hoteltrip_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trips.HotelTrip'),
        ),
    ]
