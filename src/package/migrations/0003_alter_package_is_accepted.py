# Generated by Django 3.2 on 2021-04-25 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_alter_package_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
