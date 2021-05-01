from rest_framework import serializers
from .models import LikePost, DislikePost

class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = ['user', 'content', 'photo', 'video', 'gif', 'file', 'why_content']

class DislikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DislikePost
        fields = ['user', 'content', 'photo', 'video', 'gif', 'file', 'why_content']        