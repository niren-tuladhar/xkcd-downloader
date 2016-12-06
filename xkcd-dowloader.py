import sys
import bs4
import requests
import urllib

def main():
    comicNumber = 1
    imageExists = True
    while imageExists:
        try:
            xkcdUrl = 'http://xkcd.com/' + str(comicNumber)
            imgDet = getImgDetails(xkcdUrl)
            saveImage(imgDet['imgUrl'], imgDet['fileName'], str(comicNumber))
            comicNumber = comicNumber + 1
        except:
            sys.exit()


#Returns the url and filename of the image
def getImgDetails(xkcdUrl):
    res = requests.get(xkcdUrl)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    element = str(soup.select('#comic > img'))
    imgDet = {'imgUrl': element.split('"')[3][2:], 'fileName': element.split('"')[1]}
    return imgDet



#Saves image in the directory of the script
def saveImage(imgUrl, fname, comicNumber):
    urllib.request.urlretrieve('http://' + imgUrl, comicNumber + '-' + fname + '.jpg')

   
if __name__ == '__main__':
    main()



    

    



    
