# Generated by Django 2.0.7 on 2018-07-30 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpmoauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='email2',
            field=models.EmailField(default='', max_length=255, unique=True, verbose_name='confirm email address'),
            preserve_default=False,
        ),
    ]