from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    ''' A user profile for saved info and order history'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_first_name = models.CharField(max_length=50, null=False, blank=False)
    default_last_name = models.CharField(max_length=50, null=False, blank=False)
    default_email = models.CharField(max_length=80, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def make_or_update_user_profile(sender, instance, created, **kwargs):
    ''' Make or update user profile '''
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()