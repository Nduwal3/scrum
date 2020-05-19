from django.db import models


class Albums(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)
    price = models.IntegerField()
    description = models.TextField()
    is_liked = models.BooleanField(default=False)
    img = models.ImageField(upload_to='images')
    

     # string representation of Albums
    def __str__(self):
        return self.artist + ' - ' + self.album_title + '-' 

class Song(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    # string representation of Songs
    def __str__(self):
        return self.file_type + '-' + self.song_title
