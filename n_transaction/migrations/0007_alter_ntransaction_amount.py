# Generated by Django 3.2.5 on 2021-07-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('n_transaction', '0006_alter_ntransaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ntransaction',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]