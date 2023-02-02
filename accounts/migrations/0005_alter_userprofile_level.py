# Generated by Django 4.1.5 on 2023-02-02 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_team_userprofile_team"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="level",
            field=models.CharField(
                blank=True,
                choices=[("team", "team leader"), ("member", "team member")],
                max_length=150,
                null=True,
            ),
        ),
    ]