# Generated by Django 4.1.7 on 2023-02-22 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
