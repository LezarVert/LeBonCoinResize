'''
 This programme resize the image file for the website "Le bon coin"
'''
# -*- coding: windows-1252 -*-
# pylint: disable=I0011,C0103
import shutil
import os
from PIL import Image
CONST_SIZE_FILE = 1000
def resize_image(path):
    '''Resize the file in parameter for "Le bon coin"
    Keyword arguments:
    path -- path of the image file
    size -- size of the image
    '''
    img = Image.open(path)
    wpercent = (CONST_SIZE_FILE/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((CONST_SIZE_FILE, hsize), Image.ANTIALIAS)
    img.save(path)

#copie du fichier mais il faudrait le renommer de name.jpg en name-compressed.jpg
shutil.copyfile("G:\\python.jpg", "G:\\python-compressed.jpg")
metadata = os.stat("G:\\python-compressed.jpg")
#os.remove("G:\\python-compressed.jpg")
if metadata.st_size > CONST_SIZE_FILE:
    resize_image("G:\\python-compressed.jpg")
else:
    print("Le fichier est de la bonne taille")
