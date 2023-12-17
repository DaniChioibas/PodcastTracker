from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Podcast,Episode
from .models import Review,ReviewEpisode
from .utils import searchPodcast,paginatePodcasts,searchEpisode,paginateEpisodes
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import ReviewForm,ReviewForm2
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def podcasts(request):
    allpodcasts, search_podcast=searchPodcast(request)

    numberOfResultsPerPage=6
    custom_range, allpodcasts = paginatePodcasts(request,allpodcasts,numberOfResultsPerPage)
    
    context={'allpodcasts': allpodcasts, 'search_podcast':search_podcast, 'custom_range':custom_range}
    return render(request, "podcasts/podcasts.html",context)
    
def podcast(request, pk):
    podcastObj= Podcast.objects.get(id=pk)
    form = ReviewForm()
    reviews= Review.objects.filter(podcast=podcastObj)

    if request.method=='POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.podcast = podcastObj
        review.owner = request.user.profile        
        review.save()
        
        #Update podcast ratios
        podcastObj.getVoteCount
        messages.success(request,"Your review was submited!")
        return redirect('podcast', pk=podcastObj.id)
    return render(request, "podcasts/single-podcast.html", {'podcast':podcastObj,'reviews':reviews,'form':form})

def episodes(request):
    allepisodes, search_episode=searchEpisode(request)

    numberOfResultsPerPage=6
    custom_range, allepisodes = paginateEpisodes(request,allepisodes,numberOfResultsPerPage)
    
    context={'allepisodes': allepisodes, 'search_episode':search_episode, 'custom_range':custom_range}
    return render(request, "podcasts/episodes.html",context)

def episode(request, pk):
    episodeObj= Episode.objects.get(id=pk)
    form = ReviewForm2()
    reviews= ReviewEpisode.objects.filter(episode=episodeObj)

    if request.method=='POST':
        form = ReviewForm2(request.POST)
        review = form.save(commit=False)
        review.episode = episodeObj
        review.owner = request.user.profile        
        review.save()
        
        #Update podcast ratios
        episodeObj.getVoteCount
        messages.success(request,"Your review was submited!")
        return redirect('episode', pk=episodeObj.id)
    return render(request, "podcasts/single-episode.html", {'episode':episodeObj,'reviews':reviews,'form':form})


@login_required(login_url='login')
def favorites(request):
    user=request.user
    allepisodes = Episode.objects.filter(
        reviewsEpisode__owner__user=user,
        reviewsEpisode__value=5
    )

    numberOfResultsPerPage=6
    custom_range, allepisodes = paginateEpisodes(request,allepisodes,numberOfResultsPerPage)
    
    context={'allepisodes': allepisodes,'custom_range':custom_range}
    return render(request, "podcasts/favorites.html",context)

@login_required(login_url='login')
def watched(request):
    user=request.user
    allepisodes = Episode.objects.filter(reviewsEpisode__owner__user=user)

    numberOfResultsPerPage=6
    custom_range, allepisodes = paginateEpisodes(request,allepisodes,numberOfResultsPerPage)
    
    context={'allepisodes': allepisodes,'custom_range':custom_range}
    return render(request, "podcasts/watched.html",context)