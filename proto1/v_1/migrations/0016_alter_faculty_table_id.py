# Generated by Django 4.0.1 on 2022-01-29 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_1', '0015_lab_time_table_no_of_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_table',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
