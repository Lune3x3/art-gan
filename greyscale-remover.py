import PIL
from PIL import Image
import os.path, sys

path = 'D:\\art-gan\\cropped'
dirs = os.listdir(path)
i = 0

ls = []

for item in dirs:
    filePath = os.path.join(path, item)
    if os.path.isfile(filePath):
        try:
            img = Image.open(filePath)
        except PIL.UnidentifiedImageError:
            pass
        if img.mode != 'RGB':
            ls.append(filePath)

print('getting the meat grinder ready... ')

for victim in ls:
    os.remove(victim)
    print(victim + ' has been slaughtered')
