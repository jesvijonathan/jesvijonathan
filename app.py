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

if __name__ == '__main__':
   app.run(host = '192.168.85.182', debug = True, port=5000)