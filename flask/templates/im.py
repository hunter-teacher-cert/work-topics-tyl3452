import PIL
from PIL import Image,ImageDraw

width = 640
height = 300

img = Image.new(mode="RGB",size=(width,height))
img.show()
imgd = ImageDraw.Draw(img)
imgd.line([(10,10),(50,50)],fill=(255,0,0), width = 1)
imgd.line([(50,10),(100,10)],fill=(0,0,255), width = 3)

img.save("test.jpg")