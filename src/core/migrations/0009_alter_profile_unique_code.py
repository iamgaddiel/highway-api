# Generated by Django 3.2 on 2021-04-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_profile_unique_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='unique_code',
            field=models.CharField(default='CL2Xxm4tm7', max_length=10),
        ),
    ]
