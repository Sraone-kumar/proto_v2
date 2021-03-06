# Generated by Django 3.2.8 on 2021-11-01 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty_table',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('faculty_id', models.IntegerField()),
                ('faculty_name', models.CharField(max_length=100)),
                ('No_hrs_per_week', models.IntegerField()),
                ('Department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v_1.department_table')),
                ('Designation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v_1.designation_table')),
            ],
        ),
        migrations.CreateModel(
            name='class_time_table',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('weekday_id', models.CharField(max_length=255)),
                ('timing_id', models.CharField(max_length=255)),
                ('Room_with_block', models.CharField(max_length=255)),
                ('branch', models.CharField(max_length=30)),
                ('section', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v_1.faculty_table')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v_1.subjects_table')),
            ],
        ),
    ]
