'''
 This programme resize the image file for the website "Le bon coin"
'''
# -*- coding: windows-1252 -*-
import shutil
import os
import sys
import re
from PIL import Image
CONST_SIZE_FILE = 1000
LIST_EXTENSION = ['.jpeg', '.jpg', '.gif', '.bmp', '.png']
PATERN_NAME_PY = '-py$'
def resize_image(path_resize):
    '''Resize the file in parameter for "Le bon coin"
    Keyword arguments:
    path_resize -- path of the image file
    '''
    img = Image.open(path_resize)
    wpercent = (CONST_SIZE_FILE/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((CONST_SIZE_FILE, hsize))
    img.save(path_resize)

for path in sys.argv:
    path_explode = os.path.splitext(path)
    if path_explode[1] not in LIST_EXTENSION:
        continue
    elif re.search(PATERN_NAME_PY, path_explode[0]):
        continue
    path_temp = os.path.splitext(path)[0] + "-py" + path_explode[1]
    shutil.copyfile(path, path_temp)
    metadata = os.stat(path_temp)
    if metadata.st_size > CONST_SIZE_FILE:
        resize_image(path_temp)
