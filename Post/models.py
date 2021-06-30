from django.db import models
from User.models import CustomUser, Bio
from django.utils import timezone

class LikePost(models.Model):
    bio = models.ForeignKey(
      Bio,
      on_delete=models.CASCADE,
      related_name='LikePost',
    )
    content = models.CharField(max_length=130)
    photo = models.CharField(max_length=255, blank =True, null=True)
    video = models.CharField(max_length=255, blank =True, null=True)
    gif = models.CharField(max_length=255, blank =True, null=True)
    file = models.CharField(max_length=255, blank =True, null=True)
    why_content = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)
    
    @property
    def like_post_fields(self):
      "return all the fields"
      post_list = {'id':self.id, 'content': self.content, 
      'photo': self.photo,'video':self.video, 
      'gif': self.gif, 'file': self.file,
      'why_content': self.why_content,'created_date':self.created_date,
      'user_id': self.user.id, 'username': self.user.username, 
      'first_name': self.user.first_name,
      'last_name': self.user.last_name
      }
      return post_list

class DislikePost(models.Model):
    bio = models.ForeignKey(
      Bio,
      on_delete=models.CASCADE,
      related_name='DislikePost',
      null=True, blank=True
    )
    content = models.CharField(max_length=130)
    photo = models.CharField(max_length=255, blank =True, null=True)
    video = models.CharField(max_length=255, blank =True, null=True)
    gif = models.CharField(max_length=255, blank =True, null=True)
    file = models.CharField(max_length=255, blank =True, null=True)
    why_content = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)
    @property
    def dislike_post_fields(self):
      "return all the fields"
      post_list = {'id':self.id, 'content': self.content, 
      'photo': self.photo,'video':self.video, 
      'gif': self.gif, 'file': self.file,
      'why_content': self.why_content,'created_date':self.created_date,
      'user_id': self.user.id, 'username': self.user.username, 
      'first_name': self.user.first_name,
      'last_name': self.user.last_name
      }
      return post_list

class LikePostReactions(models.Model):
    bios = models.ForeignKey(
      Bio,
      on_delete=models.CASCADE,
      related_name='LikePostReactions',
      null=True, blank=True
    )
    like_post = models.ForeignKey(
      LikePost,
      on_delete=models.CASCADE,
      related_name='LikePostReactions',
    )
    like = models.IntegerField()
    favorite = models.IntegerField()
    dislike = models.IntegerField()
    share = models.IntegerField()
    seen = models.IntegerField()
    comment = models.TextField(null=True)

    @property
    def like_reactions(self):
      "Returns the list of all fields"
      post_list = {'id':self.like_post.id, 'content': self.like_post.content, 
      'photo': self.like_post.photo,'video':self.like_post.video, 
      'gif': self.like_post.gif, 'file': self.like_post.file,
      'why_content': self.like_post.why_content,'created_date':self.like_post.created_date,
      'user_id': self.like_post.user.id, 'username': self.like_post.user.username, 
      'first_name': self.like_post.user.first_name,
      'last_name': self.like_post.user.last_name
      }
      return post_list
      @property
      def comments(self):
        return self.comment

class DisLikePostReactions(models.Model):
    bios = models.ForeignKey(
      Bio,
      on_delete=models.CASCADE,
      related_name='DisLikePostReactions',
      blank=True, null=True,
    )
    dislike_post = models.ForeignKey(
      DislikePost,
      on_delete=models.CASCADE,
      related_name='DisLikePostReactions',
    )
    like = models.IntegerField()
    favorite = models.IntegerField()
    dislike = models.IntegerField()
    share = models.IntegerField()
    seen = models.IntegerField()
    comment = models.TextField(null=True)

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