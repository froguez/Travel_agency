# Generated by Django 3.0.8 on 2020-08-26 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0036_auto_20200826_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='triptemplate',
            name='eventtrip_id',
            field=models.ForeignKey(blank=True, limit_choices_to={'ring': models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='trips.Ring')}, null=True, on_delete=django.db.models.deletion.CASCADE, to='trips.EventTrip'),
        ),
        migrations.AddField(
            model_name='triptemplate',
            name='hoteltrip_id',
            field=models.ForeignKey(blank=True, limit_choices_to={'ring': models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='trips.Ring')}, null=True, on_delete=django.db.models.deletion.CASCADE, to='trips.HotelTrip'),
        ),
    ]
