from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Podcast
from .models import Review
from .utils import searchPodcast,paginatePodcasts
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .forms import ReviewForm
from django.contrib import messages


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

