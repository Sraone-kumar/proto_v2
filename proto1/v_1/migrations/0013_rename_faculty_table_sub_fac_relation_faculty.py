# Generated by Django 3.2.8 on 2021-11-21 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v_1', '0012_sub_fac_relation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sub_fac_relation',
            old_name='faculty_table',
            new_name='faculty',
        ),
    ]