# Generated by Django 3.2.5 on 2021-07-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeepayment', '0003_alter_employeepayment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeepayment',
            name='remarks',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
