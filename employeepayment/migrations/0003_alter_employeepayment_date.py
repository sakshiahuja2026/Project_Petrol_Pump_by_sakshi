# Generated by Django 3.2.3 on 2021-07-15 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeepayment', '0002_rename_check_date_employeepayment_cheque_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeepayment',
            name='date',
            field=models.DateField(default=datetime.datetime.utcnow),
        ),
    ]
