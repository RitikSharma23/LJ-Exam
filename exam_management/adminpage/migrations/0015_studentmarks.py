# Generated by Django 4.1.3 on 2022-12-06 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminpage", "0014_alter_studentdetails_aadhaar_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentMarks",
            fields=[
                (
                    "enrollment",
                    models.CharField(max_length=16, primary_key=True, serialize=False),
                ),
            ],
        ),
    ]