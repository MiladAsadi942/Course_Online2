# Generated by Django 5.0 on 2024-03-31 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_alter_course_grammer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='grammer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
