from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import CustomUserCreationForm,ProfileForm
from podcasts.models import Episode,Podcast
from .utils import ms_to_hh_mm


from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
# Create your views here.

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('/')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, 'Account was created! Please confirm  your account on your email!')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')


def registerUser(request):

    if request.user.is_authenticated:
        return redirect('/')
    page='register'
    form=CustomUserCreationForm
    context={'page': page,'form': form}

    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.is_active=False
            user.save()

            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('/')
        else:
            messages.error(request, 'An error has occurred during registration')
            
    return render(request,'users/login_register.html',context)

def loginUser(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method=='POST':
        username=request.POST['username'].lower()
        password=request.POST['password']

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request,'Username does not exist')
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else '/')
        else:
            messages.error(request,'Username OR password is incorrect')
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def editAccount(request):
    # stats
    user=request.user
    allepisodes = Episode.objects.filter(reviewsEpisode__owner__user=user)
    allepisodes2 = Episode.objects.filter(
        reviewsEpisode__owner__user=user,
        reviewsEpisode__value=5
    )
    allepisodes_count = allepisodes.count()
    allepisodes_count2 = allepisodes2.count()
    total=0
    for episode in allepisodes:
        total+=episode.duration

    maxepisode={}
    for episode in allepisodes:
        title=episode.podcast.title
        if title not in maxepisode:
            maxepisode[title] = 1
        else:
            maxepisode[title] += 1
    if maxepisode:
        max_title = max(maxepisode, key=lambda k: maxepisode[k])
    else:
        max_title = None
    duration=ms_to_hh_mm(total)
    # end of stats
    profile=request.user.profile
    form=ProfileForm(instance=profile)
    if request.method=='POST':
        form=ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully.')
            return redirect('edit-account')
    context={'form':form,'username':profile.username,'email':profile.email,'watched':allepisodes_count,'favorites':allepisodes_count2,'duration':duration,'title':max_title}
    return render(request, 'users/profile_form.html', context)