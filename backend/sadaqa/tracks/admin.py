from django.contrib import admin
from .models import *

admin.site.register(Track)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(Playlist)
admin.site.register(ReplyComment)
admin.site.register(ReplyLike)

