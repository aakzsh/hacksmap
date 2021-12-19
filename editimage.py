
from pyffmpeg import FFmpeg
import urllib.request
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def second(pfpurl, name, followers):
    urllib.request.urlretrieve(pfpurl, "static/photo.png")
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
    my_image = Image.open("static/carousel/2.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(name, font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2 + 800), name, ((255,255,245)), font=title_font, )
    image_editable.text(((1080-w)/2 + 30,(479-h)/2 + 1100), followers, ((255,255,245)), font=title_font, )
    
    
    my_image.save('static/carousel/kardolol.png')
    im1 = Image.open('static/carousel/kardolol.png')
    im2 = Image.open('static/photo1.png')
    back_im = im1.copy()
    back_im.paste(im2, (340, 350))
    back_im.save('static/carousel/kardolmao.png', quality=100)


def fifth(name):
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 150)
    my_image = Image.open("static/carousel/5.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(name, font=title_font)
    image_editable.text(((1080-w)/2,(1920-h)/2 ), name, ((255,255,245)), font=title_font, )
    my_image.save("static/carousel/hemhe.png")

def ninth(wins):
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 150)
    my_image = Image.open("static/carousel/9.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(wins, font=title_font)
    image_editable.text(((1080-w)/2,(1920-h)/2 ), wins, ((255,255,245)), font=title_font, )
    my_image.save("static/carousel/hemhe9.png")

def tenth(proj, likes):
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 150)
    my_image = Image.open("static/carousel/10.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(likes, font=title_font)
    image_editable.text(((1080-w)/2,(1920-h)/2 - 200 ), proj+"\n\n\n\n\n"+likes, ((255,255,245)), font=title_font, )
    my_image.save("static/carousel/hemhe10.png")

def twelfth(totalteam):
    title_font = ImageFont.truetype('static/Montserrat-ExtraBold.ttf', 100)
    my_image = Image.open("static/carousel/12.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(totalteam, font=title_font)
    image_editable.text(((1080-w)/2,(1920-h)/2 + 50 ), totalteam, ((255,255,245)), font=title_font, )
    my_image.save("static/carousel/hemhe12.png")

def fourteenth(url, name):
    urllib.request.urlretrieve(url, "static/soulmate.png")
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
    my_image = Image.open("static/carousel/14.png")
    image_editable = ImageDraw.Draw(my_image)
    w, h = image_editable.textsize(name, font=title_font)
    image_editable.text(((1080-w)/2,(479-h)/2 + 800), name, ((255,255,245)), font=title_font, )
    
    
    my_image.save('static/carousel/kardolel.png')
    im1 = Image.open('static/carousel/kardolel.png')
    im2 = Image.open('static/soulmate1.png')
    back_im = im1.copy()
    back_im.paste(im2, (340, 350))
    back_im.save('static/carousel/kardolmaol.png', quality=100)
