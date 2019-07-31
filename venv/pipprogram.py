#steps to set pip path:
# open command  line:
#pip list
#How to install pillow:
# open command prompt
#Type command as pip install pillow
# To uninstall : Pip uninstall pillow

#Example script to open image

from PIL import Image as im
x = im.open("sample.png")
x.show()


#Example script to rotate as image

from PIL import Image as im
x = im.open("sample.png")
y = x.rotate(45)
y.show()


#example script for converting(Black&white) and save

from  PIL import Image as im
x = im.open("sample.png")
y = x.convert('L')
y.save("new.png")
y.show()


#After these file handling function file