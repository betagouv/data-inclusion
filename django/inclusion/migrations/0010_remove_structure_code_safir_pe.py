# Generated by Django 4.0.3 on 2022-05-03 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inclusion", "0009_remove_structure_address1_remove_structure_address2_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="structure",
            name="code_safir_pe",
        ),
    ]
