# Generated by Django 3.0.8 on 2020-08-26 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0037_auto_20200826_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triptemplate',
            name='eventtrip_id',
            field=models.ForeignKey(blank=True, limit_choices_to={'ring': '2'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='trips.EventTrip'),
        ),
        migrations.AlterField(
            model_name='triptemplate',
            name='hoteltrip_id',
            field=models.ForeignKey(blank=True, limit_choices_to={'ring': '2'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='trips.HotelTrip'),
        ),
    ]
