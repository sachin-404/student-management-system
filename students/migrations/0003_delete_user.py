# Generated by Django 4.2.1 on 2023-05-20 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
