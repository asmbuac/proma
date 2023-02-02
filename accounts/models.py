from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


LEVEL = (
    ("team", "team leader"),
    ("member", "team member"),
)


class Team(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class UserProfileManager(models.Manager):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(
        upload_to=None,
        blank=True,
        default=None,
    )
    team = models.ForeignKey(
        Team,
        related_name="members",
        on_delete=models.PROTECT,
        null=True,
    )
    level = models.CharField(
        choices=LEVEL,
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.username

    def createProfile(sender, **kwargs):
         if kwargs['created']:
            user_profile = UserProfile.objects.created(user=kwargs['instance'])

    post_save.connect(createProfile, sender=User)
