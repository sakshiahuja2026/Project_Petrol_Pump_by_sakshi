# Generated by Django 3.2.3 on 2021-07-15 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('c_payment', '0006_remove_c_payment_slipno'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_payment',
            name='slipno',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
    ]
