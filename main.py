from bs4 import BeautifulSoup
import os
import requests
import shutil

baseURL = input('URL: ')

download = []
for pageNum in range(1, 101):
    URL = baseURL + str(pageNum)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    for img in soup.find_all('img'):
        imgURL = img.attrs.get('src')
        if not imgURL:
            continue

        if imgURL not in download:
            download.append(imgURL)

    print('Done scraping: ', URL)

imgnum = 0
try:
    os.makedirs('dataset')
except FileExistsError:
    pass
for url in download:
    filename = os.path.join('dataset', 's' + str(imgnum) + '.jpeg')

    response = requests.get(url, stream = True)
    if response.status_code ==200:
        with open(filename, 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)

        print(str(imgnum) + ' out of ' + str(len(download)))
        imgnum += 1
