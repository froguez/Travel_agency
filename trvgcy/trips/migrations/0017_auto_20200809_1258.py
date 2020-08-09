# Generated by Django 3.0.8 on 2020-08-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0016_auto_20200809_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='has_suite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hotel',
            name='suite_price',
            field=models.DecimalField(decimal_places=2, default='00000', max_digits=5),
        ),
    ]
