from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

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

# class CustomUser(AbstractUser):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('N', 'Prefer not to say'),
#     )
#     date_of_birth = models.DateField(max_length=255, blank=True, null=True)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
#     terms_confirmed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.email