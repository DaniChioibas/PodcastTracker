from .models import Podcast,Episode
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def searchPodcast(request): # Search for podcasts by title
    search_podcast = ""

    if request.GET.get('search_podcast'):
        search_podcast = request.GET.get('search_podcast')

    allpodcasts= Podcast.objects.filter(title__icontains=search_podcast)
    return allpodcasts, search_podcast

def paginatePodcasts(request, allpodcasts, results): # Paginator for podcasts

    page = request.GET.get('page')
    paginator = Paginator(allpodcasts, results)

    try:
        allpodcasts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        allpodcasts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        allpodcasts = paginator.page(page)

    leftIndex = (int(page) - 3)
    if leftIndex < 1:
        leftIndex = 1

    rigtIndex = (int(page) + 3)
    if rigtIndex > paginator.num_pages:
        rigtIndex=paginator.num_pages+1

    custom_range = range(leftIndex,rigtIndex)

    return custom_range, allpodcasts

def searchEpisode(request): 
    # Search for episodes by title
    search_episode = ""

    if request.GET.get('search_episode'):
        search_episode = request.GET.get('search_episode')

    allepisodes = Episode.objects.filter(title__icontains=search_episode)
    return allepisodes, search_episode

def paginateEpisodes(request, allepisodes, results): 
    # Paginator for episodes
    page = request.GET.get('page')
    paginator = Paginator(allepisodes, results)

    try:
        allepisodes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        allepisodes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        allepisodes = paginator.page(page)

    left_index = (int(page) - 3)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 3)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, allepisodes