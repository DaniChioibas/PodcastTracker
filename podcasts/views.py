from django.shortcuts import render
from django.http import HttpResponse
from .models import Podcast
from .models import Review


def podcasts(request):
    search_podcast = ""

    if request.GET.get('search_podcast'):
        search_podcast = request.GET.get('search_podcast')

    allpodcasts= Podcast.objects.filter(title__icontains=search_podcast)
    context={'allpodcasts': allpodcasts, 'search_podcast':search_podcast}
    return render(request, "podcasts/podcasts.html",context)
    
def podcast(request, pk):
    podcastObj= Podcast.objects.get(id=pk)
    reviews= Review.objects.filter(podcast=podcastObj)
    return render(request, "podcasts/single-podcast.html", {'podcastObj':podcastObj,'reviews':reviews})