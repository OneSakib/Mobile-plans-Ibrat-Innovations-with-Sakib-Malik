# Generated by Django 4.0.4 on 2022-05-06 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airtel',
            name='mobileNo',
        ),
        migrations.RemoveField(
            model_name='bsnl',
            name='mobileNo',
        ),
        migrations.RemoveField(
            model_name='jio',
            name='mobileNo',
        ),
        migrations.RemoveField(
            model_name='mtnl',
            name='mobileNo',
        ),
        migrations.RemoveField(
            model_name='vodafone',
            name='mobileNo',
        ),
    ]
