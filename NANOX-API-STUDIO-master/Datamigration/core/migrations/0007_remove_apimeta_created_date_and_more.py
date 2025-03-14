# Generated by Django 5.0.4 on 2024-04-11 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_apimeta_dj_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apimeta',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='apimeta',
            name='python_code',
        ),
        migrations.RemoveField(
            model_name='apimeta',
            name='python_file',
        ),
        migrations.RemoveField(
            model_name='table',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='api_method',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='api_name',
            field=models.CharField(blank=True, max_length=1000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='api_property',
            field=models.TextField(blank=True, default='API_DEFAULT_PROPERTY', null=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='api_source',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='api_type',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='code_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='db_connection',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='db_connection_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='document_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='table_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='uid',
            field=models.CharField(blank=True, max_length=1000, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_data_type',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_name_public',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_rule',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_select',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='related_to',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='table_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='db_connection',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='db_connection_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='document_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='psk_uid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='relations',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_name_public',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='uid',
            field=models.CharField(blank=True, max_length=1000, null=True, unique=True),
        ),
    ]
