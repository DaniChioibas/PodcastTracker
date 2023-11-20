from django.db import models
import uuid

# Create your models here.
class Podcast(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image=models.ImageField(null=True,blank=True, default="default.jpg")
    tags= models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    vote_total=models.IntegerField(default=0, null=True,blank=True)
    vote_ratio=models.FloatField(default=0, null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='reviews')
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.podcast.title) + ' ' + str(self.rating) + ' ' + str(self.created)
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)