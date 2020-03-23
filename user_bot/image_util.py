from PIL import Image, ImageFont, ImageDraw
from config import avatar, time_av

def draw_time(time):
    image = Image.open(avatar)
    image.load()
    W, H = image.size
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font="fonts/BRUX.ttf", size=244) 
    wt, ht = draw.textsize(time, font=font)
    draw.text(((W - wt) / 2, (H - ht) / 2 - 18), time, font=font, fill="#9f1618")
    
    image.save(time_av)
