# Generated by Django 4.0 on 2022-09-21 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sql', '0008_rename_exams_user_exam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='exam',
            new_name='exams',
        ),
    ]