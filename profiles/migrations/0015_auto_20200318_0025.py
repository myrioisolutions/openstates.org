# Generated by Django 2.2.10 on 2020-03-18 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0014_auto_20200317_2359"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="usagereport", unique_together={("profile", "date", "endpoint")},
        ),
        migrations.RemoveField(model_name="usagereport", name="key",),
    ]