# Generated by Django 2.1.7 on 2019-03-29 12:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ARNN', '0019_auto_20190329_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='IS',
            field=models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(5e-324)], verbose_name='Input Scaling'),
            preserve_default=False,
        ),
    ]
