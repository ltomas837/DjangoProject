# Generated by Django 2.1.5 on 2019-03-29 08:43

import django.core.validators
from django.db import migrations, models



def template_test(apps, schema_editor):
    Template = apps.get_model('ARNN', 'Template')
    new = Template(id='0', N='10', spectral_radius='5', dim_input='3', dim_output='4', proba='0.5', seed='10', creation_date='2019-03-28 17:20', owner_id='0', lr='0.5')
    new.save()


class Migration(migrations.Migration):

    dependencies = [
        ('ARNN', '0017_corpus_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corpus',
            name='data_name',
        ),
        
        migrations.AlterField(
            model_name='template',
            name='seed',
            field=models.IntegerField(default=-1, verbose_name='Random Seed (-1 correspond to random)'),
        ),
        migrations.RunPython(template_test)
    ]
