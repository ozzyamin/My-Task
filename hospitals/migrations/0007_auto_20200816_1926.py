# Generated by Django 2.1 on 2020-08-16 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0006_auto_20200814_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='doc',
            field=models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospitals.Doctor'),
        ),
    ]
