# Generated by Django 3.2.8 on 2021-11-05 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_1', '0005_auto_20211104_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_time_table',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
