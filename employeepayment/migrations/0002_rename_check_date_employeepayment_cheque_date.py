# Generated by Django 3.2.3 on 2021-06-30 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeepayment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeepayment',
            old_name='check_date',
            new_name='cheque_date',
        ),
    ]
