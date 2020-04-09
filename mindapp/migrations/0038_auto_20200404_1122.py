# Generated by Django 2.2.10 on 2020-04-04 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mindapp', '0037_auto_20200404_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='time_r',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='situationtimer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mindapp.Player'),
        ),
    ]
