# Generated by Django 2.2.10 on 2020-04-05 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mindapp', '0044_auto_20200405_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='situationtimer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindapp.Player'),
        ),
    ]