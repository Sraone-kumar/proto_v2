# Generated by Django 3.2.8 on 2021-11-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_1', '0009_alter_subjects_table_subject_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='section_table',
            fields=[
                ('section_id', models.AutoField(primary_key=True, serialize=False)),
                ('section_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='semester_table',
            fields=[
                ('semester_id', models.AutoField(primary_key=True, serialize=False)),
                ('semester_number', models.IntegerField()),
            ],
        ),
    ]