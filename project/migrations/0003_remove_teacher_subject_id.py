# Generated by Django 5.0.6 on 2024-06-19 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_subject_teachers_alter_student_class_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subject_id',
        ),
    ]
