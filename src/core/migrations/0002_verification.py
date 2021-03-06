# Generated by Django 3.2 on 2021-04-21 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nin_number', models.ImageField(default='NIN.png', upload_to='', verbose_name='%Y/%m/%d-NIN-images')),
                ('voters_card', models.ImageField(default='voters.png', upload_to='', verbose_name="%Y/%m/%d-voter's-images")),
                ('bvn', models.CharField(max_length=12, unique=True)),
                ('self_photo', models.ImageField(default='verification.png', upload_to='%Y/%m/%d-verification-images')),
                ('is_verified', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
