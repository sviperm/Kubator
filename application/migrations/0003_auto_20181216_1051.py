# Generated by Django 2.1.4 on 2018-12-16 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20181216_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationarchive',
            name='closing_data',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата закрытия заявки'),
        ),
        migrations.AddField(
            model_name='applicationarchive',
            name='opening_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата открытия заявки'),
        ),
        migrations.AlterField(
            model_name='applicationstatus',
            name='is_application_done',
            field=models.BooleanField(default=False, verbose_name='Заявка закрыта'),
        ),
    ]
