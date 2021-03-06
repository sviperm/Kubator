# Generated by Django 2.1.4 on 2018-12-24 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedWorkerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(max_length=100, verbose_name='Отчество')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления заявки')),
                ('opening_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата открытия заявки')),
                ('closing_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия заявки')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Наименование статуса')),
                ('done', models.BooleanField(default=False, verbose_name='Заявка закрыта')),
            ],
        ),
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(max_length=100, verbose_name='Отчество')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('contact_phone', models.CharField(max_length=16, verbose_name='Контактный телефон')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Должность')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='service.PatientProfile'),
        ),
        migrations.AddField(
            model_name='order',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='service.Service'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='service.OrderStatus'),
        ),
        migrations.AddField(
            model_name='order',
            name='worker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='service.MedWorkerProfile'),
        ),
        migrations.AddField(
            model_name='medworkerprofile',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Position', verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='medworkerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
