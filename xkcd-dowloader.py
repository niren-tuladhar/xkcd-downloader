import sys, bs4, requests, urllib

#pass URL
#check url exists
    #get image
    #get title
    #save filename with the title
#else end program
def getImageUrl(xkcdUrl):
    res = requests.get(xkcdUrl)
    soup = bs4.BeautifulSoup(res.text)
    element = str(soup.select('#comic > img'))
    temp = element.split('"')[1::2]
    url = str(temp[1])
    return url[2:]


def getImageTitle(xkcdUrl):
    res = requests.get(xkcdUrl)
    soup = bs4.BeautifulSoup(res.text)
    element = soup.select('#ctitle')
    return element[0].text

def saveImage(imageUrl, fileName, comicNumber):
    urllib.request.urlretrieve('http://' + imageUrl, comicNumber + '-' + fileName + '.jpg')

    
comicNumber = 1767
imageExists = True
while imageExists:
#for comicNumber in range(1, 6):
    try:
        xkcdUrl = 'http://xkcd.com/' + str(comicNumber)
        imageUrl = getImageUrl(xkcdUrl)
        fileName = getImageTitle(xkcdUrl)
        saveImage(imageUrl, fileName, str(comicNumber))
        comicNumber = comicNumber + 1
    except:
        sys.exit() 
    
      



    

    



    
