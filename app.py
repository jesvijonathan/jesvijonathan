from flask import Flask, redirect, url_for, request, render_template, make_response, send_from_directory
from flask_mail import * 
from flask import jsonify
import json
import datetime
import pickle

app = Flask(__name__)

data = {
   'log_no' : 0,
   'dic_log' : False,
}

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

@app.route("/")
def index():
   log(request.environ)
   title = "Jesvi Jonathan"
   description = "Jesvi's Official Webpage"
   return render_template('index.html',
   title = title,
   description = description)

@app.route("/r")
def log_file():
   lfile = open("./static/log.txt", "a+")
   lfile.write("\nig")
   x = lfile.read()
   
   lfile.close()
   return make_response("deon")

def log(x=None):
   log_text =None
   
   if x == None:
      x = request.environ

#    user_details = { 
#    'REMOTE_ADDR' : x['REMOTE_ADDR'],
#    'REMOTE_PORT' : x['REMOTE_PORT'],
#    'werkzeug.socket' : x['werkzeug.socket'],
#    'HTTP_USER_AGENT' : x['HTTP_USER_AGENT'],
# }
#    user_request = {   
#    'PATH_INFO' : x['PATH_INFO'],
#    'QUERY_STRING' : x['QUERY_STRING'],
#    'RAW_URI' : x['RAW_URI'],
#    'REQUEST_URI' : x['REQUEST_URI'],
#    'werkzeug.request' : x['werkzeug.request'],
#    }
#    server = {
#    'wsgi.url_scheme' : x['wsgi.url_scheme'],
   
#    'SERVER_NAME' : x['SERVER_NAME'],
#    'SERVER_PORT' : x['SERVER_PORT'],
#    'HTTP_HOST' : x['HTTP_HOST'],
#    'SCRIPT_NAME' : x['SCRIPT_NAME'], 
#    }
#    print("\n")

   
   # # print(x)
   # y = jsonify(o)
   # # print(y)
   # xx = json.dumps(user_details, indent=4, default=str)
   
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
      msg += "Failed To Open log.txt"
      print(msg)
   
   try:
      data['log_no']+=1   
      log_id = str(data['log_no'])
      save_data()

      uip = x['REMOTE_ADDR']
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

      req_str = str(x['werkzeug.request'])
      ind1 = req_str.find(" ")
      in1 = req_str[1:ind1]
      in2 = req_str[ind1+1:] 
      ind2 = in2.find(" ")
      in2 = in2[:ind2 ]
      in3 = str(x['REQUEST_METHOD'])

      user_request = in2 + "; " + in1 + "; " + in3 

      server = str(x['HTTP_HOST'])

      log_text = (
         "[" + log_id  + "] " +
         "[" + log_time +  "] " + 
         "[" + user_ip + "]" + ip_text + " " +
         "[" + device + "] " + 
         "[" + user_request + "] " +
         "[" + server + "] "
      )      

      slog.write("\n")
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

@app.route("/geto", methods=["GET"])
def geto():
   log(request.environ)
   return make_response("Done !")

@app.route("/temp")
def temp():
   title = "Jesvi Jonathan"
   description = "Temporary & experimental stuff here !"
   return render_template('temp.html',
   title = title,
   description = description)

@app.errorhandler(404)  
def not_found(e):
  log(request.environ)
  return render_template("404.html")

if __name__ == '__main__':
   app.run(host = '192.168.85.182', debug = True, port=5000)
