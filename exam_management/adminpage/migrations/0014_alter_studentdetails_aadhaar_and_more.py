# Generated by Django 4.1.3 on 2022-12-06 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminpage", "0013_alter_studentdetails_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentdetails",
            name="aadhaar",
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="studentdetails",
            name="userid",
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]