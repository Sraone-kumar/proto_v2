# Generated by Django 3.2.8 on 2021-11-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_1', '0006_alter_class_time_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty_table',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
