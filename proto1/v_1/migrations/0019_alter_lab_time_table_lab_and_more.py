# Generated by Django 4.0 on 2022-01-30 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v_1', '0018_alter_class_time_table_faculty_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab_time_table',
            name='lab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='v_1.lab_information_table'),
        ),
        migrations.AlterField(
            model_name='lab_time_table',
            name='lab_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='v_1.subjects_table'),
        ),
    ]
