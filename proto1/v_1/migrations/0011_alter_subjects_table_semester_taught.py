# Generated by Django 3.2.8 on 2021-11-18 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v_1', '0010_section_table_semester_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects_table',
            name='semester_taught',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v_1.semester_table'),
        ),
    ]