from rest_framework import serializers
from .models import LikePost, DislikePost, Follow

class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = ['user', 'content', 'photo', 'video', 'gif', 'file', 'why_content']

    def update(self, instance, validated_data):
        instance.content = validated_data['content']
        instance.photo = validated_data['photo']
        instance.video = validated_data['video']
        instance.gif = validated_data['gif']
        instance.file = validated_data['file']
        instance.why_content = validated_data['why_content']
        instance.save()
        return instance
        
class DislikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DislikePost
        fields = ['user', 'content', 'photo', 'video', 'gif', 'file', 'why_content']        

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