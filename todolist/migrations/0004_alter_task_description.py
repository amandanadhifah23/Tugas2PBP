# Generated by Django 4.1 on 2022-10-13 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(),
        ),
    ]
