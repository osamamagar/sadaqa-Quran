from django.db import models
from accounts.models import MyUser

class Track(models.Model):
    audio = models.FileField(upload_to='tracks/audio/',null=False)
    name = models.CharField(max_length=20,null=False)
    description=models.TextField(null=True)
    image=models.ImageField(upload_to='tracks/images',)
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    




class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    likes=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

class CommentLike(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    commentLike=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Playlist(models.Model):
    name = models.CharField(max_length=50, null=False)
    image=models.ImageField(upload_to='playlist/images')
    description = models.TextField(null=True)
    tracks = models.ManyToManyField(Track, blank=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    