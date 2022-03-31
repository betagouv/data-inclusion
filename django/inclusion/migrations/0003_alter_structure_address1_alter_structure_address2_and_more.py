# Generated by Django 4.0.3 on 2022-03-31 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inclusion", "0002_structure_typologies"),
    ]

    operations = [
        migrations.AlterField(
            model_name="structure",
            name="address1",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="structure",
            name="address2",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="structure",
            name="siret",
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
