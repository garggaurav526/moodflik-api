# Generated by Django 3.2.4 on 2021-06-15 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_block_blocked_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Block',
        ),
    ]
