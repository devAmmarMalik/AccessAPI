# Python 3
# coding: utf-8

__author__ = "Ammar S Malik"
__copyright__ = "Copyright 2022, API call to IMDB"
__credits__ = ["Ammar Malik"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "all creditors/github"
__email__ = "dev.malik.ammar@gmail.com"
__status__ = "Production"

movie = ""
from distutils.log import error
import json, requests, os

def getMoviesInfo(searchFor, movieName):
    url = "https://imdb-api.com/en/API/--SearchFor--/k_d0rilf8k/"
    try:
        response = requests.get(url.replace('--SearchFor--',searchFor) + movieName)
    except requests.exceptions.Timeout:
        # Website is not responding. It timed out
        print("url timed out")

    except requests.exceptions.HTTPError as e:
        # HTTP Errored out
        print('Bad request')
        response = 0

    except requests.exceptions.InvalidURL as e:
        # Invalid URL
        print("Invalid URL")

    return response

os.system('clear')
movieTitle = input("Movie to search: ")
print("searcning. please wait ... ")
response = getMoviesInfo('SearchMovie', movieTitle)
if response.status_code == 200:
    movie = json.loads(response.text)
elif response.status_code == 404:
    print("Invalid URL parameter")
    exit()
else:
    raise ValueError("Bad request!")
    exit()

# get full cast of each movie found in the list above
#castUrl = "https://imdb-api.com/en/API/FullCast/k_d0rilf8k/"
movieCast = ''
counter=0
for i in movie['results']:
    print("Title: {} - {}".format(i['title'], i['description']))
    print("------------------------------------------------------------------")
    #response = requests.get(url.replace('--SearchFor--','FullCast') + i['id'])
    response = getMoviesInfo('FullCast', i['id'])
    if response.status_code == 200:
        movieCastData = json.loads(response.text)
        print('Directed by : ') 
        [print('        ' + eachDir) for eachDir in [directorInfo['name'] + " " + directorInfo['description'] for directorInfo in movieCastData['directors']['items']]]
        print('Written by : ') 
        [print('        ' + eachDir) for eachDir in [directorInfo['name'] + " " + directorInfo['description'] for directorInfo in movieCastData['writers']['items']]]
        print('Actors : ') 
        [print('        ' + eachDir) for eachDir in [directorInfo['name'] + " as " + directorInfo['asCharacter'] for directorInfo in movieCastData['actors'][:5]]]
    elif response.status_code == 404:
        print("Invalid URL parameter")
        exit()