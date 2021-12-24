from flask import Flask, render_template, request
import urllib.request
import glob, os
from pyffmpeg import FFmpeg
import shutil
import urllib.request
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from card import editcard
from editimage import fourteenth,  fifth,  second, ninth, seventh,  tenth, twelfth, third
import asyncio
from map import locateHacker
from utils import getdisplayname, getavatar, getfollowers, getfriendslocation, getTotalProjects, winnerandparticipated

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
    directory = username
    
    if os.path.isfile("static/users/"+directory+"/2.png") == False:
        parent_dir = "static/users/"
        path = os.path.join(parent_dir, directory)
        try:
            os.mkdir(path)
        except:
            pass
    name = getdisplayname(username).split(" ")[0]
    pfpurl = getavatar(username)
    wins, hackathons = winnerandparticipated(username)
    if hackathons==0:
        return render_template('new.html')
    projectlist, memberCount, memberLink = getTotalProjects(username)
    follower = getfollowers(username)
    topprojects = {}
    totallikes = 0

    for i in range(len(projectlist)):
        
        k = int(projectlist[i]['like'])
        totallikes += int(k)
        v = projectlist[i]['projecttitle']
        # print(topprojects)
        if k in topprojects:
            curr = topprojects[k]
            
            curr.append(v)

            topprojects[k] = curr
        else:
            topprojects[k] = [v]

    sorted_projects = sorted(topprojects.keys(), reverse=True)

    top5projects = []
    curr = ""
    for i in range(len(sorted_projects)):

        curr = topprojects[sorted_projects[i]]
        # print("curr:", curr)
        for j in curr:
            if len(top5projects) < 5:
                top5projects.append(j)

    # print(sorted_projects)
    # print("top 5", top5projects)

    try:
        bestproject = top5projects[0]
    except:
        bestproject = ""

    totalteammates = len(memberCount)
    sorted_teammates = sorted(memberCount.items(), key=lambda item: int(item[1]), reverse=True)
    # print(totalteammates, sorted(memberCount.items(), key=lambda item: int(item[1]), reverse=True))

    try:
        topteammate = sorted_teammates[0][0]
        topteammateusername = memberLink[topteammate]
        topteammateavatar = getavatar(topteammate)
    except:
        topteammate = ""
        topteammateusername = ""
        topteammateavatar = "https://i1.wp.com/devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-180.png?ssl=1"

    # print(totallikes)
    print(name, pfpurl, wins, hackathons, follower, top5projects, bestproject, totalteammates, topteammate, topteammateusername, topteammateavatar, totallikes)
    
    second(pfpurl, name, follower, username)
    third(hackathons, username)
    fifth(bestproject, username)
    seventh(top5projects, username)
    ninth(wins, username)
    tenth(str(hackathons), str(totallikes), username)
    twelfth(str(totalteammates), username)
    fourteenth(topteammateavatar,  topteammateusername, username)
    editcard(pfpurl, name, wins, bestproject, topteammateusername, username )
    return render_template('hackathon.html')

# hacker_info = []
@app.route('/map/<username>')
def map(username):
    #hackername = getdisplayname(username)
    #hackeravatar = getavatar(username)
    #projectlist, memberCount, memberLink = getTotalProjects(username)
    loc = getfriendslocation(username)
    nameAndLatlng = {}
    for hacker in loc.keys():
        if loc[hacker] != '':
            nameAndLatlng[hacker] = [locateHacker(loc[hacker]), getavatar(hacker), getdisplayname(hacker)]
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
    # await getsoulmate(soulmate_url, pfpurl, name, followers, registered, bestproj, hours, totallikes, totalproj, teammates, soulmate)
    
    return render_template('lol.html')

    
@app.route('/summary/<username>')
def summary(username):
    
    try:
        shutil.rmtree("static/users/"+username)
    except:
        pass

    return render_template('summary.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
