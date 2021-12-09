from flask import Flask, redirect, url_for, request, render_template, make_response, send_from_directory
from flask_mail import * 

app = Flask(__name__)

@app.route("/")
def index():
   title = "Jesvi Jonathan"
   description = "Jesvi's Official Webpage"
   return render_template('index.html',
   title = title,
   description = description)

@app.route("/temp")
def temp():
   title = "Jesvi Jonathan"
   description = "Temporary & experimental stuff here !"
   return render_template('temp.html',
   title = title,
   description = description)

@app.errorhandler(404)  
def not_found(e):
  return render_template("404.html")

if __name__ == '__main__':
   app.run(host = '192.168.85.182', debug = True, port=5000)
