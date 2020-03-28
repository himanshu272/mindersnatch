# Generated by Django 2.1.5 on 2020-03-28 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mindapp', '0007_auto_20200329_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='situations',
            name='option_3',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='option3', to='mindapp.option'),
        ),
        migrations.RemoveField(
            model_name='situations',
            name='option_2',
        ),
        migrations.AddField(
            model_name='situations',
            name='option_2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='option2', to='mindapp.option'),
        ),
    ]
