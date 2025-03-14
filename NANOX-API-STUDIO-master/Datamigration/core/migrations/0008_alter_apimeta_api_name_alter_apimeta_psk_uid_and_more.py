# Generated by Django 5.0.4 on 2024-04-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_apimeta_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apimeta',
            name='api_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='psk_uid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='apimeta',
            name='uid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='archived',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='field_property',
            field=models.TextField(blank=True, default='{}', null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='psk_uid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='published',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='has_media',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='has_posts',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='published',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='readonly',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='uid',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='version',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
