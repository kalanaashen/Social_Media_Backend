from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('users', UserViewSet, basename='user')
router.register('profiles', ProfileViewSet, basename='profile')
router.register('posts', PostViewSet, basename='post')
router.register('likes', LikeViewSet, basename='like')
router.register('comments', CommentViewSet, basename='comment')
router.register('followers', FollowerViewSet, basename='follower')

urlpatterns = router.urls