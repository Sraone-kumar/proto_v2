# Generated by Django 4.0.3 on 2022-05-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_1', '0025_lab_time_table_extra_faculty_lab_time_table_time_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab_time_table',
            name='extra_faculty',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='lab_time_table',
            name='time_1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lab_time_table',
            name='time_2',
            field=models.IntegerField(null=True),
        ),
    ]