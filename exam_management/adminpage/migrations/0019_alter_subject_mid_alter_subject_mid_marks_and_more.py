# Generated by Django 4.1.3 on 2022-12-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminpage", "0018_remove_subject_id_alter_subject_subjectcode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject",
            name="mid",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="subject",
            name="mid_marks",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="subject",
            name="practical",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="subject",
            name="practical_marks",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="subject",
            name="throry",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="subject",
            name="throry_marks",
            field=models.IntegerField(default=0),
        ),
    ]
