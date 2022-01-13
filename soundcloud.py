import soundcloud 
client = soundcloud.Client(client_id=YOUR_CLIENT_ID)
tracks = client.get('/users/'+USERNAME+'/tracks')
for track in tracks:
    uri = track.uri
    track_info = client.get(uri)
    plays = track_info.playback_count

    pass