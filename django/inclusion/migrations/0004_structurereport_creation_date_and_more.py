# Generated by Django 4.0.3 on 2022-04-04 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inclusion", "0003_alter_structure_address1_alter_structure_address2_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="structurereport",
            name="creation_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="structurereport",
            name="modification_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
