# Generated by Django 3.2.8 on 2021-12-03 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_1', '0014_lab_information_table_lab_time_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab_time_table',
            name='no_of_hours',
            field=models.IntegerField(null=True),
        ),
    ]
