# Generated by Django 4.2.2 on 2023-07-06 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctors',
            old_name='doc_img',
            new_name='doc_image',
        ),
    ]
