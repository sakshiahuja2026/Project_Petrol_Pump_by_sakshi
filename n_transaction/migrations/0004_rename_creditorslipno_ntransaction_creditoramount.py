# Generated by Django 3.2.3 on 2021-07-06 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('n_transaction', '0003_auto_20210706_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ntransaction',
            old_name='creditorslipno',
            new_name='creditoramount',
        ),
    ]