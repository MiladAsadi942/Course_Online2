# Generated by Django 5.0 on 2024-03-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_customer_checks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='checks',
            field=models.BooleanField(default=False),
        ),
    ]
