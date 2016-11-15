'''
 This programme resize the image file for the website "Le bon coin"
'''
# -*- coding: windows-1252 -*-
# pylint: disable=I0011,C0103
import shutil
import os
import sys
from PIL import Image
CONST_SIZE_FILE = 1000
def resize_image(path_resize):
    '''Resize the file in parameter for "Le bon coin"
    Keyword arguments:
    path_resize -- path of the image file
    '''
    img = Image.open(path_resize)
    wpercent = (CONST_SIZE_FILE/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((CONST_SIZE_FILE, hsize), Image.ANTIALIAS)
    img.save(path_resize)

#copie du fichier mais il faudrait le renommer de name.jpg en name-compressed.jpg
for path in sys.argv:
    path_explode = os.path.splitext(path)
    if path_explode[1] != ".jpg":
        continue
    print(path)
    path_temp = os.path.splitext(path)[0] + "-py.jpg"
    shutil.copyfile(path, path_temp)
    metadata = os.stat(path_temp)
    if metadata.st_size > CONST_SIZE_FILE:
        resize_image(path_temp)
    else:
        print("Le fichier est de la bonne taille")
os.system("pause")
