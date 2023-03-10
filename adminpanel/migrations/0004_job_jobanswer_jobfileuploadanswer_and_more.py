# Generated by Django 4.1 on 2022-12-28 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("adminpanel", "0003_delete_category_alter_documentmodel_adhaarfile_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(max_length=255)),
                (
                    "nature",
                    models.CharField(
                        choices=[
                            ("intern", "Intern"),
                            ("contract", "Contract"),
                            ("fulltime", "Full-Time"),
                        ],
                        max_length=255,
                    ),
                ),
                ("deadline", models.DateField()),
                ("salary_range_min", models.IntegerField(blank=True, null=True)),
                ("salary_range_max", models.IntegerField(blank=True, null=True)),
                (
                    "job_location",
                    models.CharField(
                        choices=[
                            ("andhra-pradesh", "Andhra Pradesh"),
                            ("arunachal-pradesh", "Arunachal Pradesh"),
                            ("assam", "Assam"),
                            ("bihar", "Bihar"),
                            ("chhattisgarh", "Chhattisgarh"),
                            ("goa", "Goa"),
                            ("gujarat", "Gujarat"),
                            ("haryana", "Haryana"),
                            ("himachal-pradesh", "Himachal Pradesh"),
                            ("jammu-and-kashmir", "Jammu and Kashmir"),
                            ("jharkhand", "Jharkhand"),
                            ("karnataka", "Karnataka"),
                            ("kerala", "Kerala"),
                            ("madhya-pradesh", "Madhya Pradesh"),
                            ("maharashtra", "Maharashtra"),
                            ("manipur", "Manipur"),
                            ("meghalaya", "Meghalaya"),
                            ("mizoram", "Mizoram"),
                            ("nagaland", "Nagaland"),
                            ("odisha", "Odisha"),
                            ("punjab", "Punjab"),
                            ("rajasthan", "Rajasthan"),
                            ("sikkim", "Sikkim"),
                            ("tamil-nadu", "Tamil Nadu"),
                            ("telangana", "Telangana"),
                            ("tripura", "Tripura"),
                            ("uttar-pradesh", "Uttar Pradesh"),
                            ("uttarakhand", "Uttarakhand"),
                            ("west-bengal", "West Bengal"),
                        ],
                        max_length=55,
                    ),
                ),
                ("jd", models.TextField()),
                ("eligibilty", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="JobAnswer",
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
                (
                    "date_updated",
                    models.DateTimeField(auto_now=True, verbose_name="Last Updated"),
                ),
            ],
            options={
                "verbose_name": "Answer",
                "verbose_name_plural": "Answers",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="JobFileUploadAnswer",
            fields=[
                (
                    "jobanswer_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="adminpanel.jobanswer",
                    ),
                ),
                ("File", models.FileField(blank=True, upload_to="docs")),
            ],
            options={
                "abstract": False,
            },
            bases=("adminpanel.jobanswer",),
        ),
        migrations.CreateModel(
            name="JobPreVerifiedAnswer",
            fields=[
                (
                    "jobanswer_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="adminpanel.jobanswer",
                    ),
                ),
                ("doc_id", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
            bases=("adminpanel.jobanswer",),
        ),
        migrations.CreateModel(
            name="JobTextAnswer",
            fields=[
                (
                    "jobanswer_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="adminpanel.jobanswer",
                    ),
                ),
                ("answer_text", models.TextField(max_length=1000)),
            ],
            options={
                "abstract": False,
            },
            bases=("adminpanel.jobanswer",),
        ),
        migrations.CreateModel(
            name="JobQuestion",
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
                (
                    "technique",
                    models.CharField(
                        choices=[
                            ("mcq_one", "MCQ with single possible answer"),
                            ("text", "Text based answer"),
                            ("file_upload", "File Upload answer"),
                            ("pre_verified", "Auto Upload answer"),
                        ],
                        max_length=55,
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date Created"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="Active Status"),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="question",
                        to="adminpanel.job",
                        verbose_name="Job.id",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="JobChoice",
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
                ("choice_text", models.CharField(max_length=200)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminpanel.jobquestion",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="jobanswer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="answer",
                to="adminpanel.jobquestion",
            ),
        ),
        migrations.CreateModel(
            name="JobMcqOneAnswer",
            fields=[
                (
                    "jobanswer_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="adminpanel.jobanswer",
                    ),
                ),
                (
                    "choice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminpanel.jobchoice",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("adminpanel.jobanswer",),
        ),
    ]
