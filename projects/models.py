from django.db import models
from django.conf import settings
from accounts.models import Team


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    team = models.ForeignKey(
        Team,
        related_name="projects",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
