# Generated by Django 4.2.2 on 2023-08-21 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='p_name',
            field=models.CharField(max_length=255),
        ),
    ]
