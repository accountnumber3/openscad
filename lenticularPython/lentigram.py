import os
from PIL import Image

os.chdir(os.path.dirname(os.path.abspath(__file__)))
ima = Image.open(r"colors.png")
imb = ima.transpose(method=Image.FLIP_LEFT_RIGHT)
imb.save('colorsflipped.png')
numstrips = 8
width, height = ima.size
stripwidth = round(width/numstrips)

print("width" + str(width)+ " stripwidth" + str(stripwidth))
strip = 0
h = height
x = 0
y = stripwidth

imgOut = Image.new("RGB", (width*2, height), "black")
while strip < numstrips:
	print("strip" + str(strip) + " x" + str(x) + " y" + str(y))
	strip += 1
	strip_a = ima.crop((x,0,y,h))
	strip_b = imb.crop((x,0,y,h))
	imgOut.paste(strip_a,(x,0))
	imgOut.paste(strip_b,(x+stripwidth,0))
	x=x+stripwidth
	y=y+stripwidth


imgOut.save('out.png')