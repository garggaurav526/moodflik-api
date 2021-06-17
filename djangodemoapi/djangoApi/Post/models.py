from django.db import models
from User.models import CustomUser

class LikePost(models.Model):
    user = models.ForeignKey(
      CustomUser,
      on_delete=models.CASCADE,
      related_name='LikePost'
    )
    content = models.CharField(max_length=130)
    photo = models.CharField(max_length=255, blank =True, null=True)
    video = models.CharField(max_length=255, blank =True, null=True)
    gif = models.CharField(max_length=255, blank =True, null=True)
    file = models.CharField(max_length=255, blank =True, null=True)
    why_content = models.CharField(max_length=150)

class DislikePost(models.Model):
    user = models.ForeignKey(
      CustomUser,
      on_delete=models.CASCADE,
      related_name='DislikePost'
    )
    content = models.CharField(max_length=130)
    photo = models.CharField(max_length=255, blank =True, null=True)
    video = models.CharField(max_length=255, blank =True, null=True)
    gif = models.CharField(max_length=255, blank =True, null=True)
    file = models.CharField(max_length=255, blank =True, null=True)
    why_content = models.CharField(max_length=150)

class Reactions(models.Model):
    users = models.ForeignKey(
      CustomUser,
      on_delete=models.CASCADE,
      related_name='Reactions'
    )
    like_post = models.ForeignKey(
      LikePost,
      on_delete=models.CASCADE,
      related_name='Reactions',
      blank=True,
      null=True
    )
    dislike_post = models.ForeignKey(
      DislikePost,
      on_delete=models.CASCADE,
      related_name='Reactions',
      blank=True,
      null=True
    )
    like = models.IntegerField()
    favorite = models.IntegerField()
    dislike = models.IntegerField()
    share = models.IntegerField()
    seen = models.IntegerField()
    comment = models.CharField(max_length=150)

class Follow(models.Model):
  follower = models.ForeignKey(
      CustomUser,
      on_delete=models.CASCADE,
      related_name='Follower'
      )
  following = models.ForeignKey(
      CustomUser,
      on_delete=models.CASCADE,
      related_name='Following'
      )