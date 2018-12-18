# Generated by Django 2.1.4 on 2018-12-17 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Наименование услуги')),
            ],
        ),
        migrations.CreateModel(
            name='TypeService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=120, verbose_name='Тип услуги')),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='service.TypeService'),
        ),
    ]
