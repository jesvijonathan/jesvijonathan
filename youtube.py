from googleapiclient.discovery import build
import urllib
import requests
import json

api_key = 'AIzaSyAI8G2IK-j7fcy8omEciNg2vqTZfJcE3DM'

channel_id = "UCHCOfxrbaGzMUCmwCvpCGjQ"
playlist_id = "PLKp1OMeA1chIHgqoLfI9d1TiApvhxQ1fJ"

def yt_get_channel_video_list():
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
    
    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)
    
    url = first_url
    video_links = []

    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)
        
        channel_items = []
        x = resp["items"]
        channel_items += x
        x = json.dumps(channel_items, indent=4, sort_keys=True, default=str)

        print(x)
        return x

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])
        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break     

    print(video_links)
    return video_links




def yt_get_playlist_video(playlist_id):
    youtube = build("youtube", "v3", developerKey = api_key)

    request = youtube.playlistItems().list(
        part = "snippet",
        playlistId = playlist_id,
        maxResults = 5
    )
    response = request.execute()

    playlist_items = []

    response = request.execute()
    
    x = response["items"]
    playlist_items += x
    x = json.dumps(playlist_items, indent=4, sort_keys=True, default=str)
    #request = youtube.playlistItems().list_next(request, response)

    print(x)
    return x

#yt_get_playlist_video(playlist_id)
#yt_get_channel_video_list()