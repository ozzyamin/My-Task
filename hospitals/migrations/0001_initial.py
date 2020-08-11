# Generated by Django 2.1 on 2020-08-05 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagType', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docName', models.CharField(max_length=500)),
                ('userName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patName', models.CharField(max_length=500)),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.Diagnosis')),
            ],
        ),
    ]