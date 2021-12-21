
from pyffmpeg import FFmpeg
import urllib.request
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def second(pfpurl, name, followers):
    if pfpurl[0]!='h':
        pfpurl = "https:" + pfpurl
    try:
        urllib.request.urlretrieve(pfpurl, "static/photo.png")
    except:
        urllib.request.urlretrieve("https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png", "static/photo.png")
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
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 150)
    followers_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 100)
    my_image = Image.open("static/initial/2.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(name, font=title_font)
    r , x = image_editable.textsize(followers, font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2 + 800), name, ((255,255,245)), font=title_font, )
    image_editable.text(((1080-r)/2,(479-x)/2 + 1100), followers, ((255,255,245)), font=title_font, )
    
    
    my_image.save('static/carousel/kardolol.png')
    im1 = Image.open('static/carousel/kardolol.png')
    im2 = Image.open('static/photo1.png')
    back_im = im1.copy()
    back_im.paste(im2, (340, 350))
    back_im.save('static/carousel/2.png', quality=100)

def third(name):
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 100)
    my_image = Image.open("static/initial/3.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(str(name), font=title_font)
    image_editable.text(((1080-w)/2,(1920-h)/2 ), str(name), ((255,255,245)), font=title_font, )
    my_image.save("static/carousel/3.png")

def fifth(name):
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 80)
    my_image = Image.open("static/initial/5.png")
    image_editable = ImageDraw.Draw(my_image)
    count = 0
    lol = ""
    for i in range(len(name)):
        count+=1
        if name[i]==" " and count>=15:
            count = 0
            lol=lol+ "\n"
        else:
            lol = lol + name[i]
    w, h = image_editable.textsize(lol, font=title_font)
    image_editable.text(((1080-w)/2,(1920-h)/2 ), lol, ((255,255,245)), font=title_font, )
    my_image.save("static/carousel/5.png")

def seventh(name):
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 80)
    final = ""
    count =0
    for i in name:
        count+=1
        final = final + str(count) + " " + centerbaamzi(i) + "\n"
    my_image = Image.open("static/initial/7.png")
    if len(name) == 0:
        name.append("")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(name[0], font=title_font)
    image_editable.text((50,500), final, ((61,76,245)), font=title_font, )
    my_image.save("static/carousel/7.png")


def ninth(wins):
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 150)
    my_image = Image.open("static/initial/9.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(str(wins), font=title_font)
    image_editable.text(((1080-w)/2,(1920-h)/2 ), str(wins), ((255,255,245)), font=title_font, )
    my_image.save("static/carousel/9.png")

def tenth(proj, likes):
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 150)
    my_image = Image.open("static/initial/10.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(likes, font=title_font)
    image_editable.text(((1080-w)/2,(1920-h)/2 - 200 ), proj+"\n\n\n\n\n"+likes, ((255,255,245)), font=title_font, )
    my_image.save("static/carousel/10.png")

def twelfth(totalteam):
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 100)
    my_image = Image.open("static/initial/12.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(totalteam, font=title_font)
    image_editable.text(((1080-w)/2,(1920-h)/2 + 50 ), totalteam, ((255,255,245)), font=title_font, )
    my_image.save("static/carousel/12.png")

def fourteenth(url, name):
    if url[0]!='h':
        url = "https:" + url
    try:
        urllib.request.urlretrieve(url, "static/soulmate.png")
    except:
        urllib.request.urlretrieve("https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png", "static/soulmate.png")
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
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 150)
    followers_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 100)
    my_image = Image.open("static/initial/14.png")
    image_editable = ImageDraw.Draw(my_image)
    names = name.split(" ")[0]
    if names=="Aakash" or name=="Shruti":
        names.lower()
    w, h = image_editable.textsize(names, font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2 + 800), name.split(" ")[0], ((255,255,245)), font=title_font, )
    
    
    my_image.save('static/carousel/kardolel.png')
    im1 = Image.open('static/carousel/kardolel.png')
    im2 = Image.open('static/soulmate1.png')
    back_im = im1.copy()
    back_im.paste(im2, (340, 350))
    back_im.save('static/carousel/14.png', quality=100)


def centerbaamzi(name):
    lol = ""
    count = 0
    for i in range(len(name)):
        count+=1
        if name[i]==" " and count>=15:
            count = 0
            lol=lol+ "\n" + "  "
        else:
            lol = lol + name[i]
    return lol