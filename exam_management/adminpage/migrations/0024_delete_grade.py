# Generated by Django 4.1.3 on 2022-12-09 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("adminpage", "0023_grade"),
    ]

    operations = [
        migrations.DeleteModel(
            name="grade",
        ),
    ]