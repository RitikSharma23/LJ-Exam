# Generated by Django 4.1.3 on 2022-12-16 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminpage", "0032_alter_studentdetails_aadhaar_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="credit",
            field=models.IntegerField(default=0),
        ),
    ]
