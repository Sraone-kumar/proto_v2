# Generated by Django 4.0.3 on 2022-03-24 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_1', '0021_faculty_table_faculty_short_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab_information_table',
            name='lab_short_name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]