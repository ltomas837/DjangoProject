# Generated by Django 2.1.7 on 2019-03-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ARNN', '0020_template_is'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corpus',
            name='data_in',
            field=models.FileField(default='None', upload_to='', verbose_name='Input file (must be CSV)'),
        ),
        migrations.AlterField(
            model_name='corpus',
            name='data_out',
            field=models.FileField(default='None', upload_to='', verbose_name='Output file (must be CSV)'),
        ),
        migrations.AlterField(
            model_name='template',
            name='seed',
            field=models.IntegerField(default=-1, verbose_name='Random Seed (-1 corresponds to random)'),
        ),
    ]
