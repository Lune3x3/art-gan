import PIL
from PIL import Image
import os.path, sys

path = 'D:\\art gan\\dataset'
dirs = os.listdir(path)
i = 0

for item in dirs:
    filePath = os.path.join(path, item)
    if os.path.isfile(filePath):
        try:
            img = Image.open(filePath)
        except PIL.UnidentifiedImageError:
            pass
        width, height = img.size
        if width > 255 and height > 255:
            x = (width-256)/2
            y = (height-256)/2
            cropped = img.crop((x, y, width - x, height - y))

            os.chdir('D:\\art gan')
            try:
                os.makedirs('dataset cropped')
            except FileExistsError:
                pass
            os.chdir('D:\\art gan\\dataset cropped')

            try:
                cropped.save(str(i) + '.png', 'PNG', quality = 100)
            except OSError:
                cropped.convert('RGB').save(str(i) + '.png', 'PNG', quality = 100)
            print(i)
            i += 1

