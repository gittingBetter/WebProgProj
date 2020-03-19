from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.db.models import Q
from .forms import UserForm
from django.contrib.auth.models import User

from .yt_vids import yt_search
import json
#import models.Video
from .models import Video
# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #some processing maybe
                #return render(request, 'index.html', { })
                return redirect("/")
    context = { 'form': form }
    return render(request, 'register.html', context)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # processing
                return render(request, 'index.html', { 'user': user })
                #return redirect("/")
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

def user_details(request, uname):
    #user = get_object_or_404(User, pk=uid)
    users = User.objects.all()
    user = users.get(username=uname)
    return render(request, 'profile.html', {
        'user': user
    })

def remove_user(request, uname):
    users = User.objects.all()
    user = users.get(username=uname)
    user.delete()
    return HttpResponseRedirect("/")


def remove_videos():
    videos = Video.objects.all()
    videos.delete()
    return HttpResponse(status=200)

            
remove_videos()
test = yt_search("a7x")
just_json = test[1]

array = []
i = 0

for video in test[1]:
    videos = Video()
    videos.defaultThumbnail    = video[0]['snippet']['thumbnails']['medium']['url']
    videos.width               = video[0]['snippet']['thumbnails']['medium']['width']
    videos.height              = video[0]['snippet']['thumbnails']['medium']['height']
    videos.title               = video[0]['snippet']['title']
    videos.channelId           = video[0]['snippet']['channelId']
    videos.channelTitle        = video[0]['snippet']['channelTitle']
    videos.description         = video[0]['snippet']['description']
    videos.ytId                = video[1]['items'][0]['id']
    videos.commentCount        = video[1]['items'][0]['statistics']['commentCount']
    videos.viewCount           = video[1]['items'][0]['statistics']['viewCount']
    videos.favoriteCount       = video[1]['items'][0]['statistics']['favoriteCount']
    videos.dislikeCount        = video[1]['items'][0]['statistics']['dislikeCount']
    videos.likeCount           = video[1]['items'][0]['statistics']['likeCount']
    videos.save()
    array.append(videos)
    #i = i + 1


