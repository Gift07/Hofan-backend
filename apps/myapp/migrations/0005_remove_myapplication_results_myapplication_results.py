# Generated by Django 4.0.6 on 2022-08-06 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_results_biology_alter_results_civics_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myapplication',
            name='results',
        ),
        migrations.AddField(
            model_name='myapplication',
            name='results',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='myapp.results'),
            preserve_default=False,
        ),
    ]
