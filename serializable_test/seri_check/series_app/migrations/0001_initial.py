# Generated by Django 3.2.8 on 2021-11-07 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designation_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=30)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series_app.designation_table')),
            ],
        ),
    ]
