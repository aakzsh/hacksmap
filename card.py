from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import urllib 
    
    
    
def editcard(pfpurl, name, wins, topproj, soulmate, username):    
    # urllib.request.urlretrieve(pfpurl, "static/baamzipfp.png")
    im = Image.open(f"static/users/{username}/photo.png")
    im1 = im.resize((100,100))
    im1.save(f"static/users/{username}/photo.png")
    im1 = Image.open('static/baamzi.png')
    im2 = Image.open(f"static/users/{username}/photo.png")
    back_im = im1.copy()
    back_im.paste(im2, (10, 10))
    back_im.save(f'static/users/{username}/baamzi2.png', quality=100)


    title_font = ImageFont.truetype('static/Poppins-Medium.ttf', 36)
    wins_font = ImageFont.truetype('static/Poppins-Regular.ttf', 24)
    my_image = Image.open(f"static/users/{username}/baamzi2.png")
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((210, 50 ), name, ((255,255,255)), font=title_font, )
    image_editable.text((210, 110 ), wins + " wins", (((132, 150, 132))), font=wins_font, )
    image_editable.text((60, 310 ), topproj, ((255,255,255)), font=title_font, )
    image_editable.text((60, 465 ), soulmate, ((255,255,255)), font=title_font, )
    my_image.save(f"static/{username}.png")



# editcard("https://lh3.googleusercontent.com/a-/AOh14GiUhYwZAli2YMr4ztjIlTdeL7J2YGtqYGikHIjJ?height=180&width=180", "aakash", "13", "Zanie", "frooti", "aakzsh")






























