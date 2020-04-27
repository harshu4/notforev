from PIL import Image, ImageDraw, ImageFont

img = Image.open('3.jpg')

fnt = ImageFont.truetype('./Kruti Dev 410 Regular.ttf', 225)
d = ImageDraw.Draw(img)
d.text((100, 50), "koi to hai!", font=fnt, fill=(229, 9, 20))

img.save('pil_text_font.png')