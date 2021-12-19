from flask import Flask, render_template, request
import urllib.request
import glob, os
from pyffmpeg import FFmpeg
import urllib.request
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from editmethods import fourteenth, fourth, getsoulmate, second, sixteenth, sixth, tenth, twelfth
import asyncio
from map import locateHacker
from utils import getdisplayname, getavatar, getfriendslocation, getTotalProjects, winnerandparticipated

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select/<username>')
def select(username):
    try:
        urllib.request.urlopen(f"https://www.devpost.com/{username}")
        return render_template('select.html', username=username)
    except:
        return render_template('404.html')

@app.route('/wrapped/<username>')
def wrapped(username):
    name = getdisplayname(username).split(" ")[0]
    pfpurl = getavatar(username)
    projectlist, memberCount, memberLink = getTotalProjects(username)
    wins, hackathons = winnerandparticipated(username)
    x = []
    y=[]
    for i in range(len(projectlist)):
        x.append(projectlist[i]['projecttitle'])
        y.append(projectlist[i]['like'])
    # print(x)
    # print(y)
    max = sorted(y, reverse=True)
    print(y)
    print(max)
    # lol = y.index(max)
    # print(y)
    # print(x)
    # print(x[lol])
    return render_template('wrapped.html')

# hacker_info = []
@app.route('/map/<username>')
def map(username):
    hackername = getdisplayname(username)
    hackeravatar = getavatar(username)
    projectlist, memberCount, memberLink = getTotalProjects(username)
    loc = getfriendslocation(username)
    nameAndLatlng = {}
    for hacker in loc.keys():
        if loc[hacker] != '':
            nameAndLatlng[hacker] = [locateHacker(loc[hacker]), getavatar(hacker)]
    # print(nameAndLatlng)
    return render_template('map.html', nameAndLatlng=nameAndLatlng)

@app.route('/tryvid')
async def tryvid():
    print("on tryvid path hehe")
    ff = FFmpeg()
    name = "aakash"
    followers = 19
    pfpurl = "https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/user_photos/001/420/227/datas/profile.jpg"
    registered  = 46
    bestproj = "ecstatic zanie visualise sab kuch"
    topprojs = [["url", "name"]]
    hours = 750
    totalproj = 37
    totallikes = 100
    teammates=27
    soulmate = "shruti"
    soulmate_url = "https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/user_photos/001/698/915/datas/profile.jpg"
    x = 150
    print("getting soulmate image")
    await getsoulmate(soulmate_url, pfpurl, name, followers, registered, bestproj, hours, totallikes, totalproj, teammates, soulmate)
    
    return render_template('lol.html')

    

if __name__ == "__main__":
    app.run(debug=True)
