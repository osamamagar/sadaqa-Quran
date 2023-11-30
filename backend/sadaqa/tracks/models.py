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
    reposted=models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Name Of Track : {self.name} - That Published by User : {self.user} - ID User Is : {self.user.id}"
    
    def increment_likeTrack(self):
        self.likes += 1
        self.save()

    def increment_repostedTrack(self):
        self.reposted += 1
        self.save()

    def increment_viewsTrack(self):
        self.views += 1
        self.save()



class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Like on Track  : {self.track} - By User : {self.user} - ID User Is : {self.user.id} - At : {self.created_at}"

    class Meta:
        unique_together = ['user', 'track']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.track.increment_likeTrack()



class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    commentLike = models.PositiveIntegerField(default=0)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Comment  : {self.content} - By User : {self.user} - ID User Is : {self.user.id} - At : {self.created_at}"

    def increment_like(self):
        self.commentLike += 1
        self.save()

class CommentLike(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Like on Comment  : {self.comment.content} - By User : {self.user} - ID User Is : {self.user.id} - At : {self.created_at}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.comment.increment_like()

    class Meta:
        unique_together = ['user', 'comment']





class Playlist(models.Model):
    name = models.CharField(max_length=50, null=False)
    image=models.ImageField(upload_to='playlist/images',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    tracks = models.ManyToManyField(Track, blank=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Name of Playlist : {self.name} - Created By User : {self.user} - ID User is {self.user.id}"



class ReplyComment(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    replyLike = models.PositiveIntegerField(default=0)
    replyContent = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Reply : {self.replyContent} On Comment : {self.comment.content} - By User : {self.user} - ID User Is : {self.user.id} - At : {self.created_at}"

    def increment_like(self):
        self.replyLike += 1
        self.save()
class ReplyLike(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    reply = models.ForeignKey(ReplyComment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.reply.increment_like()

    class Meta:
        unique_together = ['user', 'reply']


class RepostedTracks(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='reposted_tracks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" Repost Track  : {self.track.name} - By User : {self.user} - ID User Is : {self.user.id} - At : {self.created_at}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.track.increment_repostedTrack()

class TrackView(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"View on Track: {self.track.name} - By User: {self.user} - ID User: {self.user.id} - At: {self.created_at}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.track.increment_viewsTrack()