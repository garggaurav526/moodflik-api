# Generated by Django 3.2.4 on 2021-06-12 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_privacysettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacysettings',
            name='privacy_settings',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
