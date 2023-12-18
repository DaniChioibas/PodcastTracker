from .models import Podcast,Episode
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from dotenv import load_dotenv
import os
import base64
import json
from requests import post,get

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

def spotify(): ### Get shows
    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    def get_token():
        auth_string = client_id + ":" + client_secret
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {"grant_type": "client_credentials"}
        result = post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
        return token

    def get_auth_header(token):
        return {"Authorization": "Bearer " + token}

    def search_for_shows(token,show_name):
        url = "https://api.spotify.com/v1/search"
        headers = get_auth_header(token)
        query = f"?q={show_name}&type=show&market=US&limit=1"

        query_url=url+query
        result=get(query_url, headers=headers)
        json_result = json.loads(result.content)["shows"]["items"]
        if len(json_result) == 0:
            print("Nu am gasit show-ul " + show_name)
            return None
        return json_result[0]

    def get_shows(token, show_id):
        headers = get_auth_header(token)
        query_url = "https://api.spotify.com/v1/shows/" + show_id + "?market=US"
        result = get(query_url, headers=headers)
        json_result = result.json()
        return json_result

    ids=[]
    search_strings=["Joe Rogan", "Lex Fridman", "Huberman", "Acasa La Maruta", "Modern Wisdom"]
    token = get_token()

    for item in search_strings:
        rez=search_for_shows(token,item)
        if rez is not None:
            ids.append(rez["id"])


    for id in ids:
        rez=get_shows(token,str(id))
        try:
            Podcast.objects.get(spotifyid=rez['id'])
        except Podcast.DoesNotExist:
            Podcast.objects.create(
                title=rez['name'],
                description=rez['description'],
                spotifyid=rez['id'],
                spotifyurl=rez['external_urls']['spotify'],
                spotifyimg=rez['images'][0]['url'],
                spotifyimg2=rez['images'][1]['url'],
                )
            
def spotifyepisodes(): ### Get episodes
    load_dotenv()

    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    def get_token():
        auth_string = client_id + ":" + client_secret
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {"grant_type": "client_credentials"}
        result = post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
        return token

    def get_auth_header(token):
        return {"Authorization": "Bearer " + token}

    def get_episodes(token, show_id):
        headers = get_auth_header(token)
        query_url = "https://api.spotify.com/v1/shows/" + show_id + "/episodes?market=US&limit=20&offset=0"
        result = get(query_url, headers=headers)
        json_result = result.json()

        episodes_data = json_result.get("items", [])
        podcast=Podcast.objects.get(spotifyid=show_id)
        for episode_data in episodes_data:
            spotifyid = episode_data.get("id", "")
            existing_episode = Episode.objects.filter(spotifyid=spotifyid).first()
            if existing_episode:
                continue

            title = episode_data.get("name", "Untitled Episode")
            description = episode_data.get("description", "")
            description_html = episode_data.get("html_description","")
            release_date= episode_data.get("release_date", "")
            duration_ms= episode_data.get("duration_ms", "")
            spotifyid=episode_data.get("id","")
            spotifyurl=episode_data.get("external_urls", {}).get("spotify")
            images = episode_data.get("images", [])
            spotifyimg = images[0].get("url") if images else None
            spotifyimg2 = images[1].get("url") if len(images) >= 2 else None

            Episode.objects.create(
                title=title,
                description=description,
                description_html=description_html,
                release_date=release_date,
                duration=duration_ms,
                spotifyid=spotifyid,
                spotifyurl=spotifyurl,
                spotifyimg=spotifyimg,
                spotifyimg2=spotifyimg2,
                podcast=podcast
        )
    token=get_token()
    allpodcasts=Podcast.objects.all()
    for podcast in allpodcasts:
        show_id=podcast.spotifyid
        get_episodes(token,show_id)
    