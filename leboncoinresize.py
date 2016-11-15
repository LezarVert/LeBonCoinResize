'''
 This programme resize image files for the website "Le bon coin"
'''
# -*- coding: windows-1252 -*-
import shutil
import os
import sys
import re
from PIL import Image
CONST_SIZE_FILE = 1000 #pixel
LIST_EXTENSION = ['.jpeg', '.jpg', '.gif', '.bmp', '.png']
PATERN_NAME_PY = '-py$'
def resize_image(_path):
    '''Resize the file in parameter for "Le bon coin"
    Keyword arguments:
        _path -- path of the image file
    '''
    img = Image.open(_path)
    if img.size[0]/img.size[1] > 1:
        wpercent = (CONST_SIZE_FILE/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((CONST_SIZE_FILE, hsize))
    else:
        hpercent = (CONST_SIZE_FILE/float(img.size[1]))
        wsize = int((float(img.size[0])*float(hpercent)))
        img = img.resize((wsize, CONST_SIZE_FILE))
    img.save(_path)

def is_image_and_not_py(_path):
    '''Test the extension and if isn't a file already resize
    Keyword arguments:
        _path -- path of the file
    '''
    _path_explode = os.path.splitext(_path)
    if _path_explode[1] not in LIST_EXTENSION:
        return False
    elif re.search(PATERN_NAME_PY, _path_explode[0]):
        return False
    else:
        return True

def file_size_ok(_path):
    '''Check the size and the dimension of image before resize it
    Keyword arguments:
        _path -- path of the image
    '''
    img = Image.open(_path)
    if img.size[0] < CONST_SIZE_FILE and img.size[1] < CONST_SIZE_FILE:
        return False
    else:
        return True

def test_copy_and_resize(_path):
    '''Test, copy, and resize the image file
    Keyword arguments:
        _path -- path of the file
    '''
    if is_image_and_not_py(_path) and file_size_ok(_path):
        path_explode = os.path.splitext(_path)
        path_out = os.path.splitext(_path)[0] + "-py" + path_explode[1]
        shutil.copyfile(_path, path_out)
        resize_image(path_out)

for path in sys.argv:
    if os.path.isdir(path):
        for path_dir in os.listdir(path):
            test_copy_and_resize(path + '\\' + path_dir)
    else:
        test_copy_and_resize(path)
