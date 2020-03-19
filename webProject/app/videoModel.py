from django.db import models
from django.db.models import CharField
from django.db.models import IntegerField
from django.db.models import URLField

class Video(models.Model):
    defaultThumbnail=URLField(max_length=200)
    width=IntegerField()
    height=IntegerField()
    title=CharField(max_length=100)
    channelId=CharField(max_length=30)
    channelTitle=CharField(max_length=100)
    description=CharField(max_length=1000)
    ytId=CharField(max_length=50, primary_key=True)
    commentCount=IntegerField()
    viewCount=IntegerField()
    dislikeCount=IntegerField()
    likeCount=IntegerField()

    def __str__(self):
        return self.title