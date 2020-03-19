#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import requests
import json

DEVELOPER_KEY = "AIzaSyBz1FC1iUVz5QtJX20TYk0tM_njpcKL56c"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def yt_search(q, max_results=20,order="relevance", token=None, location=None, location_radius=None):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=q,
        type="video",
        pageToken=token,
        order = order,
        part="id,snippet",
        maxResults=max_results,
        location=location,
        locationRadius=location_radius,
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            payload = {'id': search_result["id"]["videoId"], 'part': 'statistics', 'key': DEVELOPER_KEY}
            l = requests.Session().get('https://www.googleapis.com/youtube/v3/videos', params=payload)    
            resp_dict = json.loads(l.text)
            arr = []
            arr.append(search_result)
            arr.append(resp_dict)
            videos.append(arr)
            del arr
    try:
        nexttok = search_response["nextPageToken"]
        return(nexttok, videos)
    except Exception as e:
        nexttok = "last_page"
        return(nexttok, videos)