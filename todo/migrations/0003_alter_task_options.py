# Generated by Django 4.2.7 on 2023-12-07 17:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0002_alter_task_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["-is_completed", "-created_at"]},
        ),
    ]
