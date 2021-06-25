# Generated by Django 3.2.3 on 2021-06-25 12:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20210621_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Value must be greater than 0')]),
        ),
    ]
