# Generated by Django 2.1 on 2020-08-17 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0009_auto_20200817_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='userName',
            field=models.EmailField(blank=True, max_length=500),
        ),
    ]
