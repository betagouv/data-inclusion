# Generated by Django 4.0.3 on 2022-06-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inclusion", "0018_structurereport_horaires_ouverture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="structurereport",
            name="telephone",
            field=models.TextField(blank=True, default=""),
        ),
    ]
