"""
Models include the UserProfile.
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    Credits: Boutique Ado project by Code Institute
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    default_phone_num = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    default_passport_num = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        validators=[MinLengthValidator(9, message="Does not meet the required \
            length")]
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
