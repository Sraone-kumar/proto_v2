# Generated by Django 3.2.8 on 2021-11-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department_table',
            name='department_name',
            field=models.CharField(max_length=50),
        ),
    ]
