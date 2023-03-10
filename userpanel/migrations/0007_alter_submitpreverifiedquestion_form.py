# Generated by Django 4.1 on 2022-12-26 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("adminpanel", "0002_initial"),
        ("userpanel", "0006_submitfilequestion_form"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submitpreverifiedquestion",
            name="form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="form",
                to="adminpanel.form",
            ),
        ),
    ]
