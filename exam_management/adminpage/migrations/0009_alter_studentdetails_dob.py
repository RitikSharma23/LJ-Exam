# Generated by Django 4.1.3 on 2022-12-06 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminpage", "0008_alter_studentdetails_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentdetails",
            name="dob",
            field=models.DateField(null=True),
        ),
    ]
