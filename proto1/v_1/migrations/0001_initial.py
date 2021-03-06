# Generated by Django 3.2.8 on 2021-11-01 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department_table',
            fields=[
                ('department_id', models.IntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Designation_table',
            fields=[
                ('designation_id', models.IntegerField(primary_key=True, serialize=False)),
                ('designation_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='subjects_table',
            fields=[
                ('subject_id', models.IntegerField(primary_key=True, serialize=False)),
                ('subject_code', models.CharField(max_length=30)),
                ('subject_name', models.CharField(max_length=200)),
                ('subject_credits', models.IntegerField()),
                ('Elective_type', models.CharField(max_length=50)),
                ('semester_taught', models.IntegerField()),
            ],
        ),
    ]
