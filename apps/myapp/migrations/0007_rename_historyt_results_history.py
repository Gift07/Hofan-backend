# Generated by Django 4.0.6 on 2022-08-06 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_myapplication_selected_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='Historyt',
            new_name='History',
        ),
    ]
