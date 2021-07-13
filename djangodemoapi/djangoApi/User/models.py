from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
import datetime

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_seconds_since_creation(self):
        """
        Find how much time has been elapsed since creation, in seconds.
        This function is timezone agnostic, meaning this will work even if
        you have specified a timezone.
        """
        return (datetime.datetime.utcnow() -
                self.created_at.replace(tzinfo=None)).seconds


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Prefer not to say'),
    )
    date_of_birth = models.DateField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    terms_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Bio(models.Model):
    user = models.ForeignKey(
      CustomUser,
      on_delete=models.CASCADE,
      related_name='Bio'
    )
    phone_number = models.CharField(max_length=12)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null=True)
    me = models.CharField(max_length=30)
    like = models.CharField(max_length=50)
    dislike = models.CharField(max_length=50)
    photo_url = models.CharField(max_length=255, blank =True, null=True)
    cover_photo_url = models.CharField(max_length=255, blank =True, null=True)
    @property
    def bio_details(self):
        "Returns the list of all fields"
        post_list = {'id':self.user.id, 'email':self.user.email,
         'username':self.user.username, 'profile_image':self.photo_url,
         'cover_image':self.cover_photo_url}
        return post_list

class PostSettings(models.Model):
    user = models.ForeignKey(
      CustomUser,
      on_delete=models.CASCADE,
      related_name='PostSettings'
    )
    privacy_settings = models.IntegerField(default=0, blank =True, null=True)

class ShareBioSettings(models.Model):
    user = models.ForeignKey(
      CustomUser,
      on_delete=models.CASCADE,
      related_name='ShareBioSettings'
    )
    setting = models.IntegerField(default=0, blank =True, null=True)

class ShowLikeDisLikeSettings(models.Model):
    user = models.ForeignKey(
      CustomUser,
      on_delete=models.CASCADE,
      related_name='ShowLikeDisLikeSettings'
    )
    setting = models.IntegerField(default=0, blank =True, null=True)

class Block(models.Model):
    user = models.ForeignKey(
      CustomUser,
      on_delete=models.CASCADE,
      related_name='Block'
    )
    blocked_user = models.ForeignKey(
      CustomUser,
      on_delete=models.CASCADE,
      related_name='blocked_user'
    )

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()


class EmailOTPs(BaseModel):
    email = models.EmailField()
    otp = models.IntegerField(default=0)
    is_used = models.BooleanField(default=False)