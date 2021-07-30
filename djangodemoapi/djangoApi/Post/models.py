from django.db import models
from User.models import CustomUser, Bio,BaseModel
from django.utils import timezone

class LikePost(BaseModel):
    bio = models.ForeignKey(
      Bio,
      on_delete=models.CASCADE,
      related_name='LikePost',
        null=True,
        blank=True
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
        post_list = {'post_id': self.id, 'why_content': self.why_content, 'file': self.file, 'gif': self.gif,
             'video': self.video, 'photo': self.photo, 'content': self.content,'created_at':self.created_date,
                   'updated_at': self.updated_at,
        'user_id': self.bio.user.id, 'username': self.bio.user.username,
        'first_name': self.bio.user.first_name,
        'last_name': self.bio.user.last_name,
                   'profile_image': self.bio.photo_url,
        }
        return post_list

    @property
    def reactions(self):
        filtered_reactions = LikePostReactions.objects.filter(like_post__id=self.id)
        favorites = filtered_reactions.filter(favorite=1).values_list('bios__user_id', flat=True)
        like = filtered_reactions.filter(like=1).values_list('bios__user_id', flat=True)
        dislike = filtered_reactions.filter(dislike=1).values_list('bios__user_id', flat=True)
        share = filtered_reactions.filter(share=1).values_list('bios__user_id', flat=True)
        seen = filtered_reactions.filter(seen=1).values_list('bios__user_id', flat=True)
        comment = filtered_reactions.filter(comment__isnull=False).values_list('bios__user_id', flat=True)
        return {
             'favorites': favorites, 'like': like,
             'dislike': dislike, 'share': share, 'seen': seen,
             'comment': comment, }

class DislikePost(BaseModel):
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
      'last_name': self.user.last_name,
                   'profile_image': self.bio.photo_url,
      }
      return post_list

    @property
    def reactions(self):
        filtered_reactions = DisLikePostReactions.objects.filter(dislike_post__id=self.id)
        favorites = filtered_reactions.filter(favorite=1).values_list('bios__user_id', flat=True)
        like = filtered_reactions.filter(like=1).values_list('bios__user_id', flat=True)
        dislike = filtered_reactions.filter(dislike=1).values_list('bios__user_id', flat=True)
        share = filtered_reactions.filter(share=1).values_list('bios__user_id', flat=True)
        seen = filtered_reactions.filter(seen=1).values_list('bios__user_id', flat=True)
        comment = filtered_reactions.filter(comment__isnull=False).values_list('bios__user_id', flat=True)
        return {
             'favorites': favorites, 'like': like,
             'dislike': dislike, 'share': share, 'seen': seen,
             'comment': comment, }


class LikePostReactions(BaseModel):
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
      'last_name': self.like_post.user.last_name,
                   'profile_image': self.like_post.user.photo_url,
      }
      return post_list
      @property
      def comments(self):
        return self.comment

class DisLikePostReactions(BaseModel):
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

    @property
    def like_reactions(self):
        "Returns the list of all fields"
        post_list = {'id': self.dislike_post.id, 'content': self.dislike_post.content,
                     'photo': self.dislike_post.photo, 'video': self.dislike_post.video,
                     'gif': self.dislike_post.gif, 'file': self.dislike_post.file,
                     'why_content': self.dislike_post.why_content, 'created_date': self.dislike_post.created_date,
                     'user_id': self.dislike_post.user.id, 'username': self.dislike_post.user.username,
                     'first_name': self.dislike_post.user.first_name,
                     'last_name': self.dislike_post.user.last_name,
                     'profile_image': self.dislike_post.user.photo_url,
                     }
        return post_list

        @property
        def comments(self):
            return self.comment


class Follow(BaseModel):
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