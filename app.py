from flask import Flask, redirect, url_for, request, render_template, make_response, send_from_directory
from flask_mail import * 
from flask import jsonify
import json
import datetime
import pickle 
# from uritemplate.api import expand 

app = Flask(__name__)

data = {
   'log_no' : 0,
   'dic_log' : False,

   'links_1' : { "https://www.youtube.com/playlist?list=PLKp1OMeA1chJ_vjA8RR9waZmUdkRa0QGN" },
   'links_2' : {"https://www.youtube.com/embed/videoseries?list=PLMsztBiO4ogZnNd9_qJul4cmlt3EC-9yB" },
   
   'yt_1' : "https://www.youtube.com/channel/UCle1DoWYu4gfKW3YQKezwsw",
   'yt_2' : "https://www.youtube.com/channel/UCHCOfxrbaGzMUCmwCvpCGjQ",
   'proj_more' : "https://github.com/jesvijonathan",
   
   'sec1' : "/home",
   'sec2' : "/artist_profile",
   'sec3' : "/content_creation_lobby",
   'sec4' : "/project_history",

   'hamb' : { 
      '0' : {
         '0'  : 'About',
         '1'  : '#secl',},
      '1' : {
         '0'  : 'Latest',
         '1'  : '#sec2',},
      '2' : {
         '0'  : 'Blog',
         '1'  : '#sec3',},
      '3' : {
         '0'  : 'Contact',
         '1'  : '#scel',},
      '4' : {
         '0'  : 'Social',
         '1'  : '#',},
   }
   
}

@app.route("/")
def index():
   log(request.environ)
   title = "Jesvi Jonathan"
   description = "Jesvi's Official Webpage"

   return render_template(
      'index.html',
      
      title = title,
      description = description,
      
      links_1 = data['links_1'],
      links_2 = data['links_2'],
      
      yt_1 = data['yt_1'],
      yt_2 = data['yt_2'],
      
      proj_more = data['proj_more'],

      sec1 = data['sec1'],
      sec2 = data['sec2'],
      sec3 = data['sec3'],
      sec4 = data['sec4'],

      hamb= data['hamb']
      )

ip = []
l = "\n"

try:
   with open('data.pickle', 'rb') as handle:
      data = pickle.load(handle)
   l += "-Data Loaded\n"
except:
   l += "-Reset Data (Failed To Load Data)"
   with open('data.pickle', 'wb') as handle:
      pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

try:
   with open('ip.pickle', 'rb') as handle:
      ip = pickle.load(handle)
   l += "-IP List Loaded\n"
except : 
   with open('ip.pickle', 'wb') as handle:
      pickle.dump(ip, handle, protocol=pickle.HIGHEST_PROTOCOL)
   l+= "-Reset IP List (Failed To Load Ip List)\n"

print(l)

def save_ip_list():
   try:
      with open('ip.pickle', 'wb') as handle:
         pickle.dump(ip, handle, protocol=pickle.HIGHEST_PROTOCOL)
      return "-IP List Saved"
   except:
      return "-Failed To Save IP List"

def save_data():
   try:
      with open('data.pickle', 'wb') as handle:
         pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
      return "-Data Saved"
   except:
      return "-Failed To Save Data"


@app.route('/ltest')
def log(x=None):
   log_text =None
   
   if x == None:
      x = request.environ 
      
   msg = ""
   
   dl = data['dic_log']

   if dl == True:
      try:
         lfile = open("./static/dic_log.txt", "a+")
         lfile.write("\n\n")
      except:
         msg += "Failed To Open dic_log.txt\n"
         print(msg)
   
   try:
      slog = open("./static/log.txt", "a+")
   except: 
      slog = open("/home/jesvi/jesvijonathan/static/log.txt", "a+")
 
   
   try:
      data['log_no']+=1   
      log_id = str(data['log_no'])
      save_data()

      if request.headers.getlist("X-Forwarded-For"):
         uip = request.headers.getlist("X-Forwarded-For")[0]
      else:
         try:
            uip = request.remote_addr
         except:
            uip = x['REMOTE_ADDR']
      # print(request.headers['X-Real-IP'])
      
      ip_exists = False

      if uip in ip:
         ip_exists = True
         ip_text = ""
      else:
         ip.append(uip)
         print(save_ip_list())
         ip_text = " [New_IP] "

      

      
      log_time = str(datetime.datetime.now().strftime("%x %X"))
      
      hua_text = str(x['HTTP_USER_AGENT'])
      device = hua_text[(hua_text.find("(")+1):(hua_text.find(")"))]

      uip = str(uip)
      user_ip =  uip + " :" + str(x['REMOTE_PORT'])

      # req_str = str(x['werkzeug.request'])
      # ind1 = req_str.find(" ")
      # in1 = req_str[1:ind1]
      # in2 = req_str[ind1+1:] 
      # ind2 = in2.find(" ")
      # in2 = in2[:ind2 ]
      # in3 = str(x['REQUEST_METHOD'])

      # user_request = in2 + "; " + in1 + "; " + in3 
      user_request = str(x['werkzeug.request'])
      #server = str(x['HTTP_HOST'])

      log_text = (
         "\n[" + log_id  + "] " +
         "[" + log_time +  "] " + 
         "[" + user_ip + "]" + ip_text + " " +
         "[" + device + "] " + 
         "[" + user_request + "] " #+
         #"[" + server + "]"
      )      

      slog.write("")
      slog.write(log_text)
      print(log_text,"\n")

      if dl == True:
         x = { 
            'id':log_id,
            'time':log_time,
            'ip': uip,
            'ip_exists':ip_exists,
            'data' : x,
            }
         o = json.dumps(x, indent=4, default=str)

         lfile.write(o)
         lfile.close()
 
   except Exception as e:
      print(e)

   if x== None:
      return True
   else:
      return render_template('debug.html', here=log_text)



@app.route('/yt2', defaults={'path': 'PLKp1OMeA1chIHgqoLfI9d1TiApvhxQ1fJ'})
@app.route('/yt2/<path:path>')
def youtube_refresh_2(path="PLKp1OMeA1chIHgqoLfI9d1TiApvhxQ1fJ"):
   # print(playlist_id)
   playlist_id = path
   if playlist_id == None:
      log(request.environ)
      playlist_id = "PLKp1OMeA1chIHgqoLfI9d1TiApvhxQ1fJ"
   
   yt_dict = yt_get_playlist_video(playlist_id)
   st = {}
   try:
      for i in range(0,len(yt_dict)):
         iss = str(yt_dict[i]["snippet"]["resourceId"]["videoId"])
         iss = "https://www.youtube.com/embed/" + str(iss) +"?controls="
         st[i] = iss    
   
   except Exception as e:
      print(e)
      st = ""
      st =str(e)

   return st


@app.route('/yt1', defaults={'path': 'PLKp1OMeA1chJ_vjA8RR9waZmUdkRa0QGN'})
@app.route('/yt1/<path:path>')
def youtube_refresh_1(path="PLKp1OMeA1chJ_vjA8RR9waZmUdkRa0QGN"):
   # print(playlist_id)
   playlist_id = path
   if playlist_id == None:
      log(request.environ)
      playlist_id = "PLKp1OMeA1chJ_vjA8RR9waZmUdkRa0QGN"
   
   yt_dict = yt_get_playlist_video(playlist_id)
   st = {}
   try:
      for i in range(0,len(yt_dict)):
         iss = str(yt_dict[i]["snippet"]["resourceId"]["videoId"])
         iss = "https://www.youtube.com/embed/" + str(iss) +"?controls=0"
         st[i] = iss   
   except Exception as e:
      print(e)
      st = ""
      st =str(e)
   
   #st = json.dumps(st) 
   return st 

@app.route('/yt')
def youtube_refresh( ):
   log(request.environ)
   links_1 = youtube_refresh_1()
   links_2 = youtube_refresh_2()
   
   data['links_1'] = links_1
   data['links_2'] = links_2

   # print(data )
   save_data()

   return data
   # /yt to refresh yt1 & yt2
   # /yt1 or yt2 to refresh seperately
   # /yt1/playlist_id or /yt2/playlist_id


@app.route('/jdata/<daa>')
@app.route('/jdata')
def da(daa="keys"):
   log(request.environ)
   if daa == "keys":
      save_data()
      return data
   elif daa == "key":
      res = dict.fromkeys(data, 0)
      return res
   else:
      return data[daa]

@app.route('/logger/<live>')
@app.route('/logger')
def logg(live=None):
   print(live)
   
   l = file = None

   try:
      with open('./static/log.txt', 'r') as file:
         l = file.read()
   except:
      with open('/home/jesvi/jesvijonathan/static/log.txt', 'r') as file:
         l = file.read()

   # print(l)
   meta = meta_time = ""
   if live!=None:
      meta = "refresh"
      meta_time = live

   return render_template('debug.html',n=l, script="1",style="body {font-size: 14px;}", meta=meta, meta_time=meta_time)

@app.route("/temp")
def temp():
   log(request.environ)
   title = "Jesvi Jonathan"
   description = "Temporary & experimental stuff here !"
   return render_template('temp.html',
   title = title,
   description = description)

@app.errorhandler(404)  
def not_found(e):
  log(request.environ)
  return render_template("404.html")

@app.route('/alink')  
def admin_links():
  log(request.environ)
  
  text = {
     'logging' : { 
         "log_file" : '/static/log.txt',
         "logs" : ['logger', 'logger/<int-time>']},
      
      'data' : { 
         "get_data_dict" : ['/jdata' , '/jdata/key', '/jdata/<key>'],
         "all_youtube" : "/yt",
         "youtubte_links_1_music_refresh" : [ "/yt1", "/yt1/play_list_id" ],
         "youtubte_links_2_video_refresh" : [ "/yt2", "/yt2/play_list_id" ]},

      'test_link' : {
         "log_test" : '/ltest',
         "temporary_embed_soundcloud" : '/temp',
         "test_links_view" : "/alink",
         "error_404" : "/<any>",
         },
      
      'website' : {
         'home/main_page' : "/",
      }

  }
  return make_response(text)

from googleapiclient.discovery import build
import urllib
import requests
import json

api_key = 'AIzaSyAI8G2IK-j7fcy8omEciNg2vqTZfJcE3DM'

channel_id = "UCHCOfxrbaGzMUCmwCvpCGjQ"


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
     
    # x = json.dumps(playlist_items, indent=4, sort_keys=True, default=str)
    #request = youtube.playlistItems().list_next(request, response)

    # print(x)
    return x

# yt_get_playlist_video(playlist_id)
#yt_get_channel_video_list()

if __name__ == '__main__':
   app.run(host = '192.168.85.182', debug = True, port=5000)
