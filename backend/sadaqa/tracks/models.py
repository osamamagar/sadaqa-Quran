from django.db import models
from accounts.models import MyUser
from django.core.exceptions import ValidationError
from django.contrib.admin.sites import site as admin_site


class Track(models.Model):
    audio = models.FileField(upload_to='tracks/audio/',null=False)
    name = models.CharField(max_length=20,null=False)
    description=models.TextField(null=True)
    image=models.ImageField(upload_to='tracks/images',null=True,blank=True)
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    




class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Like on Track  : {self.track} - By User : {self.user} - At : {self.created_at}"


class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    commentLike = models.PositiveIntegerField(default=0)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Comment  : {self.content} - By User : {self.user} - At : {self.created_at}"


class CommentLike(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Like on Comment  : {self.comment.content} - By User : {self.user} - At : {self.created_at}"





class Playlist(models.Model):
    name = models.CharField(max_length=50, null=False)
    image=models.ImageField(upload_to='playlist/images',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    tracks = models.ManyToManyField(Track, blank=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



    