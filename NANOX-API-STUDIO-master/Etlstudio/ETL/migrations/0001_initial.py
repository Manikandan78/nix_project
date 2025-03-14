# Generated by Django 4.2.4 on 2024-03-11 09:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='connections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_engine', models.CharField(choices=[('postgresql', 'postgresql'), ('mysql', 'mysql')], default='postgresql', max_length=100)),
                ('driver', models.CharField(choices=[('psycopg2', 'psycopg2'), ('mysqlconnector', 'mysqlconnector')], default='psycopg2', max_length=100)),
                ('host', models.CharField(max_length=100)),
                ('database', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('schema', models.CharField(blank=True, max_length=100, null=True)),
                ('port', models.IntegerField(blank=True, default=5432, null=True)),
                ('connection_name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'connections',
            },
        ),
        migrations.CreateModel(
            name='service_timer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeinterval', models.PositiveIntegerField(blank=True, default=3, null=True)),
                ('time_period', models.CharField(blank=True, choices=[('byinterval', 'Time Interval'), ('hour', 'Hourly'), ('day', 'Daily'), ('week', 'Weekly')], max_length=50, null=True)),
                ('minutes_for_hour', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(59)])),
                ('time_for_day', models.TimeField(blank=True, null=True)),
                ('day_name_for_week', models.CharField(blank=True, choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=50, null=True)),
                ('time_for_week', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'service_timer',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(blank=True, max_length=100, null=True)),
                ('source_api', models.CharField(max_length=100, unique=True)),
                ('priority', models.IntegerField(default=100)),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('method', models.CharField(blank=True, choices=[('POST', 'POST'), ('UPDATE', 'UPDATE')], default='POST', max_length=250, null=True)),
                ('start_task', models.DateTimeField(blank=True, null=True)),
                ('end_task', models.DateTimeField(blank=True, null=True)),
                ('interval', models.PositiveIntegerField(blank=True, default=3, null=True)),
                ('run_separate', models.BooleanField(default=False)),
                ('last_executed', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('connection_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedules_set', to='ETL.connections')),
            ],
            options={
                'db_table': 'schedules',
                'unique_together': {('url', 'method')},
            },
        ),
    ]
