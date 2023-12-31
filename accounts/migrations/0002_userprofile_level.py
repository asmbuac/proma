# Generated by Django 4.1.5 on 2023-01-31 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="level",
            field=models.CharField(
                blank=True,
                choices=[
                    ("admin", "administrator"),
                    ("team", "team leader"),
                    ("member", "team member"),
                ],
                max_length=150,
                null=True,
            ),
        ),
    ]
