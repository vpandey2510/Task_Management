# Generated by Django 4.1.13 on 2024-10-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0002_alter_task_category_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('work', 'Work'), ('personal', 'Personal'), ('other', 'Others')], default='Choose any', max_length=10),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='Choose any', max_length=10),
        ),
    ]
