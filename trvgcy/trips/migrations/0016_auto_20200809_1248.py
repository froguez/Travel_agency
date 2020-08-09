# Generated by Django 3.0.8 on 2020-08-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0015_auto_20200809_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ring',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=False, max_length=40, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='all_inclusive_price',
            field=models.DecimalField(decimal_places=2, default='00000', max_digits=5),
        ),
        migrations.AddField(
            model_name='hotel',
            name='breakfast_price',
            field=models.DecimalField(decimal_places=2, default='00000', max_digits=4),
        ),
        migrations.AddField(
            model_name='hotel',
            name='double_room_price',
            field=models.DecimalField(decimal_places=2, default='00000', max_digits=5),
        ),
        migrations.AddField(
            model_name='hotel',
            name='full_board_price',
            field=models.DecimalField(decimal_places=2, default='00000', max_digits=5),
        ),
        migrations.AddField(
            model_name='hotel',
            name='half_board_price',
            field=models.DecimalField(decimal_places=2, default='00000', max_digits=5),
        ),
        migrations.AddField(
            model_name='hotel',
            name='kindergarden_price',
            field=models.DecimalField(decimal_places=2, default='00000', max_digits=4),
        ),
        migrations.AddField(
            model_name='hotel',
            name='single_price',
            field=models.DecimalField(decimal_places=2, default='00000', max_digits=5),
        ),
        migrations.AddField(
            model_name='hotel',
            name='spa_price',
            field=models.DecimalField(decimal_places=2, default='00000', max_digits=4),
        ),
    ]
