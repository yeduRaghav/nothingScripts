import requests
from time import sleep
from bs4 import BeautifulSoup

domain = 'http://robert-adams.info/'
response = requests.get(domain)
soup = BeautifulSoup(response.content, 'html.parser')

paths = []
for path in soup.find_all('a'):
    if path.get('href').find('.mp3') != -1:
        paths.append(path.get('href'))


#downloadDirectory =


for index, path in enumerate(paths):
    fileUrl = domain+path
    response = requests.get(fileUrl)
    with open(r"/Users/yeduraghav/Desktop/nothingtalks/"+path, 'wb') as blobFile:
        blobFile.write(response.content)
    print("Downloaded "+str(index)+"/"+str(len(paths))+" : "+ path)
    sleep(10)


#fileUrl = domain+paths[0]
#audioFile = requests.get(fileUrl)
#with open(r'/Users/yeduraghav/Desktop/nothingtalks/'+paths[0], 'wb') as ff:
#    ff.write(audioFile.content)
