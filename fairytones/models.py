from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='documents/')
    song = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.name
     
class Playlist(models.Model):
    watch_id = models.AutoField(primary_key=True)  # Renamed to playlist_id
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=1000000, default="")

class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=10000000, default="")
from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='documents/')
    song = models.FileField(upload_to='documents/')
    
    def __str__(self):
        return self.name
     
class Playlist(models.Model):
    watch_id = models.AutoField(primary_key=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=1000000, default="")

class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=10000000, default="")