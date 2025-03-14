# Generated by Django 5.0.4 on 2024-04-10 05:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_apimeta_table_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apimeta',
            name='api_method',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='api_name',
            field=models.CharField(max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='api_source',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='api_type',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='db_connection_name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='document_url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='psk_uid',
            field=models.CharField(default=uuid.uuid4, max_length=1000),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='uid',
            field=models.CharField(max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_data_type',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_name_public',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='field',
            name='psk_uid',
            field=models.CharField(default=uuid.uuid4, max_length=1000),
        ),
        migrations.AlterField(
            model_name='field',
            name='related_to',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='field',
            name='table_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='table',
            name='db_connection_name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='table',
            name='document_url',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='table',
            name='psk_uid',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='table',
            name='relations',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_name',
            field=models.CharField(max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_name_public',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='table',
            name='uid',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]
