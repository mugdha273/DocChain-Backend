# Generated by Django 4.1 on 2023-01-07 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("adminpanel", "0006_remove_jobchoice_question_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="adhaarfile",
            name="File",
        ),
        migrations.RemoveField(
            model_name="birthcertificate",
            name="File",
        ),
        migrations.RemoveField(
            model_name="castecertificate",
            name="File",
        ),
        migrations.RemoveField(
            model_name="disabilitycertificate",
            name="File",
        ),
        migrations.RemoveField(
            model_name="domicilecertificate",
            name="File",
        ),
        migrations.RemoveField(
            model_name="hsc",
            name="File",
        ),
        migrations.RemoveField(
            model_name="incomecertificate",
            name="File",
        ),
        migrations.RemoveField(
            model_name="jeeallotmentletter",
            name="File",
        ),
        migrations.RemoveField(
            model_name="jeemarksheet",
            name="File",
        ),
        migrations.RemoveField(
            model_name="medicalcertificate",
            name="File",
        ),
        migrations.RemoveField(
            model_name="migrationcertificate",
            name="File",
        ),
        migrations.RemoveField(
            model_name="nationalitycertificate",
            name="File",
        ),
        migrations.RemoveField(
            model_name="pan",
            name="File",
        ),
        migrations.RemoveField(
            model_name="passport",
            name="File",
        ),
        migrations.RemoveField(
            model_name="sportscertificate",
            name="File",
        ),
        migrations.RemoveField(
            model_name="ssc",
            name="File",
        ),
        migrations.RemoveField(
            model_name="transfercertificate",
            name="File",
        ),
    ]
