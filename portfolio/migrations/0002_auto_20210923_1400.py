# Generated by Django 3.1.2 on 2021-09-23 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='descrition',
            new_name='description',
        ),
    ]
