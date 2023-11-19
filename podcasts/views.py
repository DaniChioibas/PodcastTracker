from django.shortcuts import render
from django.http import HttpResponse
from .models import Podcast
from .models import Review


def podcasts(request):
    allpodcasts= Podcast.objects.all()
    context={'allpodcasts': allpodcasts}
    return render(request, "podcasts/podcasts.html",context)
    
def podcast(request, pk):
    podcastObj= Podcast.objects.get(id=pk)
    reviews= Review.objects.filter(podcast=podcastObj)
    return render(request, "podcasts/single-podcast.html", {'podcastObj':podcastObj,'reviews':reviews})