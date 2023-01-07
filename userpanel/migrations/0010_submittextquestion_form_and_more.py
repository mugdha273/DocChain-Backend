# Generated by Django 4.1 on 2023-01-06 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("adminpanel", "0006_remove_jobchoice_question_and_more"),
        ("userpanel", "0009_alter_submitpreverifiedquestion_question"),
    ]

    operations = [
        migrations.AddField(
            model_name="submittextquestion",
            name="form",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="adminpanel.form",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="submitfilequestion",
            name="form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="adminpanel.form"
            ),
        ),
        migrations.AlterField(
            model_name="submitpreverifiedquestion",
            name="form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="adminpanel.form"
            ),
        ),
        migrations.AlterField(
            model_name="submittextquestion",
            name="answer",
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name="JobSubmitTextQuestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("answer", models.TextField(blank=True)),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminpanel.form",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminpanel.jobquestion",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobSubmitPreVerifiedQuestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=200, null=True)),
                ("file_id", models.IntegerField(blank=True, null=True)),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminpanel.form",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminpanel.jobquestion",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobSubmitFileQuestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("answer", models.FileField(blank=True, upload_to="docs")),
                (
                    "form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminpanel.form",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminpanel.jobquestion",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]