# Generated by Django 2.2.10 on 2020-04-04 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mindapp', '0041_auto_20200404_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='time',
            field=models.CharField(default='April 6, 2020 18:30:00', max_length=40),
        ),
        migrations.AlterField(
            model_name='situationtimer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindapp.Player'),
        ),
    ]
