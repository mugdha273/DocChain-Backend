# Generated by Django 4.1 on 2022-08-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userpanel", "0005_submitpreverifiedquestion_file_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="submitfilequestion",
            name="form",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
