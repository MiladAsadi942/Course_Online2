# Generated by Django 5.0 on 2024-03-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='catagorey'),
        ),
    ]
