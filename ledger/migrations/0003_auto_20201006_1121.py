# Generated by Django 2.2.8 on 2020-10-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_auto_20201006_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='client_timestamp',
            field=models.BigIntegerField(),
        ),
    ]
