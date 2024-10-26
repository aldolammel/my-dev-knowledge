from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User, UserProfileOne, UserProfileTwo


# Creates and associates one of UserProfile types to the new User:
@receiver(post_save, sender=User)
def user_profile_auto_creation(sender, instance, created, **kwargs):
    if created:
        if instance.profile_type == '1':
            UserProfileOne.objects.create(user=instance)
        else:
            UserProfileTwo.objects.create(user=instance)
