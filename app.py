from flask import Flask, render_template, request
import urllib.request
import glob, os
from pyffmpeg import FFmpeg
import urllib.request
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np
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
    return render_template('wrapped.html')

@app.route('/map/<username>')
def map(username):
    return render_template('map.html')

@app.route('/tryvid')
def tryvid():
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
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', x)
    urllib.request.urlretrieve(soulmate_url, "static/soulmate.png")
    urllib.request.urlretrieve(pfpurl, "static/photo.png")
    im = Image.open("static/soulmate.png")
    im1 = im.resize((400,400))
    im1.save('static/soulmate1.png')
    img=Image.open("static/soulmate1.png").convert("RGB")
    npImage=np.array(img)
    h,w=img.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((npImage,npAlpha))
    Image.fromarray(npImage).save('static/soulmate2.png')
    print("getting pfp")
    im = Image.open("static/photo.png")
    im1 = im.resize((400,400))
    im1.save('static/photo1.png')
    img=Image.open("static/photo1.png").convert("RGB")
    npImage=np.array(img)
    h,w=img.size
    alpha = Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((npImage,npAlpha))
    Image.fromarray(npImage).save('static/photo2.png')
 
    print("applying edits on 2nd frame")
    # 2
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 150)
    lol = name.split(" ")[0]
    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(lol, font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2), lol, ((255,255,245)), font=title_font, )
    my_image.save('static/kardolol.png')
    
    ff.options(f"-i static/parts/2.mp4 -i static/kardolol.png -filter_complex overlay=0:700 static/final/2.mp4")
    # ff.options(f"-i static/final/2.mp4 -i static/photo2.png -filter_complex overlay=350:300 static/final/21.mp4")
    # title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 100)
    # lol = str(followers)
    # my_image = Image.open("static/bg.png")
    # image_editable = ImageDraw.Draw(my_image)
    # w, h = image_editable.textsize(str(followers), font=title_font)
    # image_editable.text(((1080-w)/2,(479-h)/2), str(followers), ((255,255,245)), font=title_font, )
    # my_image.save('static/kardolol.png')
    # ff.options(f"-i static/final/21.mp4 -i static/kardolol.png -filter_complex overlay=0:1000 static/final/22.mp4")
    # 4
    print("applying edits on 4th frame")
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 100)
    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    hehe = 140
    if len(str(registered))>2:
        hehe = 100
    elif len(str(registered)) == 1:
        hehe = 180
        
    image_editable.text((30,30), str(registered), ((255,209,0)), font=title_font, )
    my_image.save('static/kardo.png')
    
    ff.options(f"-i static/parts/4.mp4 -i static/kardo.png -filter_complex overlay={hehe-40}:875 static/final/4.mp4")
    # 6
    print("applying edits on 6th frame")
    if len(bestproj)>20:
        bestproj = bestproj[0:20]+".."
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 80)
    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(bestproj, font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2), str(bestproj), ((255,255,255)), font=title_font, )
    my_image.save('static/kardolol.png')
    
    ff.options(f"-i static/parts/6.mp4 -i static/kardolol.png -filter_complex overlay=0:800 static/final/6.mp4")    
    # 8

    # 10
    print("applying edits on 10th frame")
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 120)
    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(str(hours), font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2), str(hours), ((255,255,255)), font=title_font, )
    my_image.save('static/kardolol.png')
    
    ff.options(f"-i static/parts/10.mp4 -i static/kardolol.png -filter_complex overlay=-240:600 static/final/10.mp4")

    # 12
    print("applying edits on 12th frame")
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 180)
    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(str(totalproj), font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2), str(totalproj), ((255,209,0)), font=title_font, )
    my_image.save('static/kardolol.png')
    
    ff.options(f"-i static/parts/12.mp4 -i static/kardolol.png -filter_complex overlay=0:500 static/final/12.mp4")

    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(str(totallikes), font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2), str(totallikes), ((255,209,0)), font=title_font, )
    my_image.save('static/kardolol.png')
    
    ff.options(f"-i static/final/12.mp4 -i static/kardolol.png -filter_complex overlay=0:1300 static/final/121.mp4")
    # 14
    print("applying edits on 14th frame")
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 100)
    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    hehe = 140
    if len(str(teammates))>2:
        hehe = 100
    elif len(str(teammates)) == 1:
        hehe = 180
        
    image_editable.text((30,30), str(teammates), ((61,76,245)), font=title_font, )
    my_image.save('static/kardo.png')
    
    ff.options(f"-i static/parts/14.mp4 -i static/kardo.png -filter_complex overlay={hehe}:970 static/final/14.mp4")
    # 16
    print("applying edits on 16th frame")
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 150)
    lol = soulmate.split(" ")[0]
    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(lol, font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2), lol, ((61,76,245)), font=title_font, )
    my_image.save('static/kardolol.png')
    
    ff.options(f"-i static/parts/16.mp4 -i static/kardolol.png -filter_complex overlay=0:900 static/final/16.mp4")
    ff.options(f"-i static/final/16.mp4 -i static/soulmate2.png -filter_complex overlay=350:400 static/final/161.mp4")

    print("defining vids baamzi for merge")
    vid_1 = VideoFileClip("static/parts/1.mp4")
    vid_2 = VideoFileClip("static/final/2.mp4")
    vid_3 = VideoFileClip("static/parts/3.mp4")
    vid_4 = VideoFileClip("static/final/4.mp4")
    vid_5 = VideoFileClip("static/parts/5.mp4")
    vid_6 = VideoFileClip("static/final/6.mp4")
    vid_7 = VideoFileClip("static/parts/7.mp4")
    vid_8 = VideoFileClip("static/parts/8.mp4")
    vid_9 = VideoFileClip("static/parts/9.mp4")
    vid_10 = VideoFileClip("static/final/10.mp4")
    vid_11 = VideoFileClip("static/parts/11.mp4")
    vid_12 = VideoFileClip("static/final/121.mp4")
    vid_13 = VideoFileClip("static/parts/13.mp4")
    vid_14 = VideoFileClip("static/final/14.mp4")
    vid_15 = VideoFileClip("static/parts/15.mp4")
    vid_16 = VideoFileClip("static/final/161.mp4")
    vid_17 = VideoFileClip("static/parts/17.mp4")

    print("starting merge in a sec")
    final_video= concatenate_videoclips([vid_1,vid_2,vid_3,vid_4,vid_5,vid_6,vid_7,vid_8,vid_9,vid_10,vid_11,vid_12,vid_13,vid_14,vid_15,vid_16,vid_17])
    print("writing final vid file")
    final_video.write_videofile("static/final_video.mp4")

    print("doneeeeeeeeeee")

    print("removing useless file")
    dir = 'static/final/'
    filelist = glob.glob(os.path.join(dir, "*mp4"))
    for f in filelist:
        os.remove(f)
    return render_template('lol.html')

if __name__ == "__main__":
    app.run(debug=True)