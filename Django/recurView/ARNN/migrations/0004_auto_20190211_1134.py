# Generated by Django 2.1.3 on 2019-02-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ARNN', '0003_network_template'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='corpus',
            options={'ordering': ['creation_date']},
        ),
        migrations.AlterModelOptions(
            name='network',
            options={'ordering': ['creation_date']},
        ),
        migrations.AlterModelOptions(
            name='template',
            options={'ordering': ['creation_date']},
        ),
        migrations.AlterField(
            model_name='template',
            name='dim_input',
            field=models.IntegerField(verbose_name='Dimension of input'),
        ),
        migrations.AlterField(
            model_name='template',
            name='input_bias',
            field=models.BooleanField(verbose_name='Input bias'),
        ),
        migrations.AlterField(
            model_name='template',
            name='proba',
            field=models.FloatField(verbose_name='Probability of a connection'),
        ),
        migrations.AlterField(
            model_name='template',
            name='spectral_radius',
            field=models.FloatField(verbose_name='Spectral radius'),
        ),
    ]
