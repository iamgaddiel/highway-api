# Generated by Django 3.2 on 2021-04-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_profile_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_code',
            field=models.CharField(editable=False, max_length=10),
        ),
    ]
