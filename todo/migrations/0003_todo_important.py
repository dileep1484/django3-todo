# Generated by Django 3.0.3 on 2020-05-10 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_important'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
