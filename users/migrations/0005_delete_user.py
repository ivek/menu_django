# Generated by Django 4.1.7 on 2023-02-22 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]