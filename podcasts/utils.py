from .models import Podcast
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