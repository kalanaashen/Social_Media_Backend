from django.db import models



class User(models.Model):
    
    username = models.CharField(max_length=50)
    email = models.EmailField()

    
    def __str__(self):
        return self.username
    
    
class Profile(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    bio=models.CharField(max_length=80,null=True,blank=True)
    avatar = models.ImageField(upload_to="avatar/", null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
    
    
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False,related_name="posts")
    image=models.ImageField(upload_to="posts/")
    caption=models.CharField(max_length=50,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.user}-{self.image}"

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="likes")
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="likes")
   
    class Meta:
        unique_together = ['user', 'post']
    
    def __str__(self):
        return f"{self.user}-{self.post}"
    
    
class Follower(models.Model):
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name="followings")
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name="followers")
    
       
    def __str__(self):
        return f"{self.follower}- {self.following}"
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    text=models.CharField(max_length=100,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.post}-{self.text}"