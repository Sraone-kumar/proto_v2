# Generated by Django 4.0 on 2022-01-17 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v_1', '0015_lab_time_table_no_of_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab_time_table',
            name='lab_faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='v_1.faculty_table'),
        ),
    ]
