from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    auth_link = "http://www.last.fm/api/auth/?api_key=" + os.environ['LASTFM_KEY']
    return render_template('home.html', auth_link=auth_link)

@app.route("/auth_callback")
def auth_callback(token):
    return token

def api_auth():
    return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
