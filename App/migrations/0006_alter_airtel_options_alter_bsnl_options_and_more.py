# Generated by Django 4.0.4 on 2022-05-06 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_airtel_options_alter_bsnl_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airtel',
            options={'verbose_name_plural': 'Airtel'},
        ),
        migrations.AlterModelOptions(
            name='bsnl',
            options={'verbose_name_plural': 'BSNL'},
        ),
        migrations.AlterModelOptions(
            name='jio',
            options={'verbose_name_plural': 'JIO'},
        ),
        migrations.AlterModelOptions(
            name='mtnl',
            options={'verbose_name_plural': 'MTNL'},
        ),
        migrations.AlterModelOptions(
            name='vodafone',
            options={'verbose_name_plural': 'Vodafone'},
        ),
    ]