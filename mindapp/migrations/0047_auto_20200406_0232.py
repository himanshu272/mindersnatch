# Generated by Django 2.2.10 on 2020-04-05 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mindapp', '0046_auto_20200406_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='visible',
        ),
        migrations.AlterField(
            model_name='situationtimer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindapp.Player'),
        ),
    ]
