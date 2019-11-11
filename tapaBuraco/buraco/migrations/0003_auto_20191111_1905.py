# Generated by Django 2.2.7 on 2019-11-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buraco', '0002_auto_20191111_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buraco',
            name='user',
            field=models.ManyToManyField(blank=True, to='buraco.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='holesDetected',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='totalAvgAcc',
            field=models.FloatField(blank=True),
        ),
    ]
