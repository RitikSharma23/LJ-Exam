# Generated by Django 4.1.3 on 2022-12-04 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminpage", "0005_rename_student_details_studentdetails"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("institute_Code", models.IntegerField()),
                ("program_code", models.IntegerField()),
                ("type", models.IntegerField()),
                ("institute_Name", models.CharField(max_length=100)),
                ("degree_Name", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("branch", models.CharField(max_length=100)),
            ],
        ),
    ]