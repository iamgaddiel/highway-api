# Generated by Django 3.2 on 2021-04-25 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_profile_user_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_code',
            new_name='unique_code',
        ),
    ]