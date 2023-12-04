from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Podcast(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image=models.ImageField(null=True,blank=True, default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    vote_total=models.IntegerField(default=0, null=True,blank=True)
    vote_ratio=models.FloatField(default=0, null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    spotifyid = models.CharField(max_length=200,null=True, blank=True)
    spotifyurl = models.CharField(max_length=2048,null=True, blank=True)
    spotifyimg = models.CharField(max_length=2048,null=True, blank=True)



    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-vote_total','-vote_ratio']

    @property
    def getVoteCount(self):
        reviews = self.reviews.all()
        upVote1 =reviews.filter(value=1).count()
        upVote2 =reviews.filter(value=2).count()
        upVote3 =reviews.filter(value=3).count()
        upVote4 =reviews.filter(value=4).count()
        upVote5 =reviews.filter(value=5).count()
        upVote = 1*upVote1 + 2*upVote2 + 3*upVote3 + 4*upVote4 + 5*upVote5
        totalVotes=reviews.count()
        ratio = (upVote/totalVotes)
        self.vote_total=upVote5+upVote4+upVote3+upVote2+upVote1
        self.vote_ratio=ratio
        self.save()

    @property
    def reviewers(self):
        queryset = self.reviews.all().values_list('owner__id',flat=True)
        return queryset
    
class Episode(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(null=True, blank=True)
    spotifyid = models.CharField(max_length=200,null=True, blank=True)
    spotifyurl = models.CharField(max_length=2048,null=True, blank=True)
    spotifyimg = models.CharField(max_length=2048,null=True, blank=True)
    release_date = models.CharField(max_length=30)
    featured_image=models.ImageField(null=True,blank=True, default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    vote_total=models.IntegerField(default=0, null=True,blank=True)
    vote_ratio=models.FloatField(default=0, null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    podcast = models.ForeignKey('Podcast', null=True, blank=True, on_delete=models.CASCADE, related_name='episodes')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created']

    @property
    def getVoteCount(self):
        reviewsEpisode = self.reviewsEpisode.all()
        upVote1 =reviewsEpisode.filter(value=1).count()
        upVote2 =reviewsEpisode.filter(value=2).count()
        upVote3 =reviewsEpisode.filter(value=3).count()
        upVote4 =reviewsEpisode.filter(value=4).count()
        upVote5 =reviewsEpisode.filter(value=5).count()
        upVote = 1*upVote1 + 2*upVote2 + 3*upVote3 + 4*upVote4 + 5*upVote5
        totalVotes=reviewsEpisode.count()
        ratio = (upVote/totalVotes)
        self.vote_total=upVote5+upVote4+upVote3+upVote2+upVote1
        self.vote_ratio=ratio
        self.save()

    @property
    def reviewers(self):
        queryset = self.reviewsEpisode.all().values_list('owner__id',flat=True)
        return queryset

    
class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True,blank=True)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='reviews')
    value = models.IntegerField(choices=RATING_CHOICES)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together=[['owner','podcast']]

    def __str__(self):
        return str(self.value) + str(self.body)
    
class ReviewEpisode(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True,blank=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='reviewsEpisode')
    value = models.IntegerField(choices=RATING_CHOICES)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together=[['owner','episode']]

    def __str__(self):
        return str(self.value) + str(self.body)
    