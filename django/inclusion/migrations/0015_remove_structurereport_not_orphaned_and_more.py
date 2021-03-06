# Generated by Django 4.0.3 on 2022-05-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inclusion", "0014_remove_structurereport_id_antenne_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="structurereport",
            name="not_orphaned",
        ),
        migrations.RemoveField(
            model_name="structurereport",
            name="structure",
        ),
        migrations.AddConstraint(
            model_name="structurereport",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("parent_report__isnull", True), ("rna__isnull", True), ("siret__isnull", True), _negated=True
                ),
                name="not_orphaned",
            ),
        ),
        migrations.DeleteModel(
            name="Structure",
        ),
    ]
