# Generated by Django 2.1.4 on 2018-12-24 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20181224_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='medworkerprofile',
            name='raw_password',
            field=models.CharField(default='password', max_length=8, verbose_name='Пароль'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientprofile',
            name='raw_password',
            field=models.CharField(default='password', max_length=8, verbose_name='Пароль'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medworkerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='patientprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
