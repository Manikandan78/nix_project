# Generated by Django 5.0.4 on 2024-04-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_apimeta_python_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apimeta',
            name='python_file',
            field=models.TextField(blank=True, null=True),
        ),
    ]
