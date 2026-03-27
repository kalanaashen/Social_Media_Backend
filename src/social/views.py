from django.shortcuts import render
from .models import *
from rest_framework import viewsets,filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response



class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class=UserSerializer
    
    
    def get_queryset(self):
        
        return User.objects.filter(id=self.request.user.id)
    
    
    def get_permissions(self):
        if self.action=='create':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    
    @action(detail=True ,methods=['get'])
    def search(self,requsest):
        keyword=self.query_params.get("q")
        users=User.objects.filter(username__icontains=keyword)
        
        return Response([
            {"id": u.id, "username": u.username}
            for u in users
        ])
    
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
        
class PostViewSet(viewsets.ModelViewSet):

   
    def get_serializer_class(self):
       
       if self.action=='create':
           return PostCreateSerializer
       return PostResponseSerializer
   
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)
   
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
        
    @action(detail=True, methods=['post'])
    def comment(self,request,pk=None):
        post=self.get_object()
        text=request.data.get('text')
        Comment.objects.create(user=request.user,text=text,post=post)
        
        return Response({"message":"commented!"})
    
    @action(detail=True, methods=['post'])
    def like(self,request,pk=None):
        post=self.get_object()
        user=request.user
    
        Like.objects.create(user=user,post=post)
        return Response({"message":"Like Added"})
    
    
    @action(detail=True ,methods=['post'])
    def unlike(self,request,pk=None):
        
        post=self.get_object()
        user=request.user
        
        Like.objects.filter(user=user,post=post).delete()
        
        return Response({"message":"Like removed!"})
    
    @action(detail=True ,methods=['get'])
    def count(self,request,pk=None):
        post=self.get_object()
        comment=post.comments.count()
        like=post.likes.count()
        
        return Response({
            "like":like,
            "comment":comment
            
        })
        
    @action(detail=False ,methods=['get'])
    
    def myactivity(self,request):
        stats_likes=Likes.objects.filter(user=request.user).count()
        stats_comments=Comment.objects.filter(user=request.user).count()
        
        
        return Response({
            "likes":stats_likes,
            "comments":stats_comments
        })
   
class LikeViewSet(viewsets.ModelViewSet):
    queryset=Like.objects.all()
    serializer_class=LikeSerializer
    

    
class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    
    
    
class FollowerViewSet(viewsets.ModelViewSet):
    serializer_class=FollowerSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Follower.objects.filter(follower=self.request.user)

    @action(detail=True, methods=['post'])
    def follow(self,request,pk=None):
        user_to_follow=User.objects.get(id=pk)
        
        user=request.user
        Follower.objects.create(follower=request.user,following=user_to_follow)
        return Response ({"message":"user followed!"})
    
    
    
    
    @action(detail=True , methods=['post'])
    
    def unfollow(self,request,pk=None):
        
        user_to_unfollow=User.objects.get(id=pk)
        user=request.user
        Follower.objects.filter(follower=user,following=user_to_unfollow).delete()
        
        return Response({"message":"user unfollowed!"})
    
