from rest_framework import serializers
from .models import LikePost, DislikePost, Follow

class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = ['bio','content', 'photo', 'video', 'gif', 'file', 'why_content']

class LikePostShow(serializers.ModelSerializer):
    post_id = serializers.ReadOnlyField(source='id')
    user_id = serializers.ReadOnlyField(source='bio.user.id')
    username = serializers.ReadOnlyField(source='bio.user.username')
    first_name = serializers.ReadOnlyField(source='bio.user.first_name')
    last_name = serializers.ReadOnlyField(source='bio.user.last_name')
    profile_image = serializers.ReadOnlyField(source='bio.user.profile_image')

    class Meta:
        model = LikePost
        # fields = ['like_post_fields','reactions']
        fields = ['post_id','user_id','username','first_name','last_name','profile_image','why_content','file','gif','video','photo','content','created_at','updated_at','reactions']


class DisLikePostShow(serializers.ModelSerializer):
    post_id = serializers.ReadOnlyField(source='id')
    user_id = serializers.ReadOnlyField(source='bio.user.id')
    username = serializers.ReadOnlyField(source='bio.user.username')
    first_name = serializers.ReadOnlyField(source='bio.user.first_name')
    last_name = serializers.ReadOnlyField(source='bio.user.last_name')
    profile_image = serializers.ReadOnlyField(source='bio.user.profile_image')

    class Meta:
        model = LikePost
        # fields = ['like_post_fields','reactions']
        fields = ['post_id','user_id','username','first_name','last_name','profile_image','why_content','file','gif','video','photo','content','created_at','updated_at','reactions']


class DislikePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = DislikePost
        fields = ['bio', 'content', 'photo', 'video', 'gif', 'file', 'why_content']

    def update(self, instance, validated_data):
        instance.content = validated_data['content']
        instance.photo = validated_data['photo']
        instance.video = validated_data['video']
        instance.gif = validated_data['gif']
        instance.file = validated_data['file']
        instance.why_content = validated_data['why_content']
        instance.save()
        return instance

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['follower', 'following']