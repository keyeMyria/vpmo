# Generated by Django 2.0.7 on 2018-07-23 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vpmoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'permissions': (('created_obj', 'Admin Level Permissions'), ('contribut_obj', 'Contributor Level Permissions'), ('read_obj', 'Read Level Permissions'))},
        ),
    ]
