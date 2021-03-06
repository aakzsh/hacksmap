
from PIL import Image, ImageDraw, ImageFont
import urllib
from flask import Flask, render_template, request
from pyffmpeg import FFmpeg
from moviepy.editor import *
import glob
import numpy as np
async def getsoulmate(soulmate_url, pfpurl, name, followers, registered, bestproj, hours, totallikes, totalproj, teammates, soulmate):
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
    print("get data done")
    return second(name, followers, registered, bestproj, hours, totallikes, totalproj, teammates,soulmate)


def second(name, followers, registered, bestproj, hours, totallikes, totalproj, teammates,soulmate):
    print("2nd")
    ff = FFmpeg()
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 150)
    lol = name.split(" ")[0]
    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(lol, font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2), lol, ((255,255,245)), font=title_font, )
    my_image.save('static/kardolol.png')
    
    ff.options(f"-i static/parts/2.mp4 -i static/kardolol.png -filter_complex overlay=0:700 static/final/2.mp4")
    ff.options(f"-i static/final/2.mp4 -i static/photo2.png -filter_complex overlay=350:300 static/final/21.mp4")
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 100)
    lol = str(followers)
    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(str(followers), font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2), str(followers), ((255,255,245)), font=title_font, )
    my_image.save('static/kardolol.png')
    ff.options(f"-i static/final/21.mp4 -i static/kardolol.png -filter_complex overlay=0:1000 static/final/22.mp4")
    return fourth(registered, bestproj, hours, totallikes, totalproj, teammates,soulmate)


def fourth(registered, bestproj, hours, totallikes, totalproj, teammates,soulmate):
    print("4th")
    ff = FFmpeg()
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
    return sixth(bestproj, hours, totallikes, totalproj, teammates,soulmate)

def sixth(bestproj, hours, totallikes, totalproj, teammates,soulmate):
    print("6th")
    ff = FFmpeg()
    if len(bestproj)>20:
        bestproj = bestproj[0:20]+".."
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 80)
    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(bestproj, font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2), str(bestproj), ((255,255,255)), font=title_font, )
    my_image.save('static/kardolol.png')
    
    ff.options(f"-i static/parts/6.mp4 -i static/kardolol.png -filter_complex overlay=0:800 static/final/6.mp4")
    return tenth(hours, totallikes, totalproj, teammates,soulmate)

def tenth(hours, totallikes, totalproj, teammates,soulmate):
    print("10th")
    ff = FFmpeg()
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 120)
    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(str(hours), font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2), str(hours), ((255,255,255)), font=title_font, )
    my_image.save('static/kardolol.png')
    
    ff.options(f"-i static/parts/10.mp4 -i static/kardolol.png -filter_complex overlay=-240:600 static/final/10.mp4")
    return twelfth(totallikes, totalproj, teammates,soulmate)

def twelfth(totallikes, totalproj, teammates,soulmate):
    print("12th")
    ff= FFmpeg()
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
    return fourteenth(teammates,soulmate)

def fourteenth(teammates,soulmate):
    print("14th")
    ff=FFmpeg()
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
    return sixteenth(soulmate)

def sixteenth(soulmate):
    print("16th")
    ff=FFmpeg()
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 150)
    lol = soulmate.split(" ")[0]
    my_image = Image.open("static/bg.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(lol, font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2), lol, ((61,76,245)), font=title_font, )
    my_image.save('static/kardolol.png')
    
    ff.options(f"-i static/parts/16.mp4 -i static/kardolol.png -filter_complex overlay=0:900 static/final/16.mp4")
    ff.options(f"-i static/final/16.mp4 -i static/soulmate2.png -filter_complex overlay=350:400 static/final/161.mp4")
    return defvid()

def defvid():
    print("defining vids")
    vid_1 = VideoFileClip("static/parts/1.mp4")
    vid_2 = VideoFileClip("static/final/22.mp4")
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
    final_video= concatenate_videoclips([vid_1,vid_2,vid_3,vid_4,vid_5,vid_6,vid_7,vid_8,vid_9,vid_10,vid_11,vid_12,vid_13,vid_14,vid_15,vid_16,vid_17])
    final_video.write_videofile("static/final_video.mp4")
    return removebaamzi()

def removebaamzi():
    print("removing useless shiz")
    dir = 'static/final/'
    filelist = glob.glob(os.path.join(dir, "*"))
    for f in filelist:
        os.remove(f)
    return 0