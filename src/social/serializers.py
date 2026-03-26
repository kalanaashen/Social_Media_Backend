from rest_framework import serializers
from .models import *



class UserSerializer(serializers.ModelSerializer):
    
    password=serializers.CharField(write_only=True)
    
    class Meta:
        model=User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    
class  ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Profile
        fields = ['id', 'user', 'bio', 'avatar']
        
    
class PostCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Post
        fields=['image','caption']
        
        
class PostResponseSerializer(serializers.ModelSerializer):
    
    user=serializers.StringRelatedField()
    
    class Meta:
        model=Post
        fields = ['id', 'user', 'image', 'caption', 'created_at']
    

class LikeSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Like
        fields="__all__"


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Comment
        fields="__all__"
        
        
        
class FollowerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Follower
        fields="__all__"