# Generated by Django 3.0.6 on 2020-06-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_stu_question_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu_question',
            name='choice',
            field=models.CharField(default='E', max_length=3),
        ),
    ]
