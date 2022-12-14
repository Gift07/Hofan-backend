# Generated by Django 4.0.6 on 2022-08-05 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_results_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='subject',
            new_name='Biology',
        ),
        migrations.AddField(
            model_name='myapplication',
            name='disability',
            field=models.CharField(default='None', max_length=255, verbose_name='Disability'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='results',
            name='Civics',
            field=models.CharField(default='C', max_length=2, verbose_name='Subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='results',
            name='English',
            field=models.CharField(default='C', max_length=2, verbose_name='Subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='results',
            name='Geography',
            field=models.CharField(default='A', max_length=2, verbose_name='Subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='results',
            name='Historyt',
            field=models.CharField(default='B', max_length=2, verbose_name='Subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='results',
            name='Kiswahili',
            field=models.CharField(default='A', max_length=2, verbose_name='Subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='results',
            name='Mathematics',
            field=models.CharField(default='A', max_length=2, verbose_name='Subject'),
            preserve_default=False,
        ),
    ]
