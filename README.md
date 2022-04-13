# AccessAPI
Access IMDB api to show movie information

## Introduction
We are accessing IMDB Api calls using Python and displaying the information on the screen if we find a movie.

There are some commands that I learned in the process that I want to highlight

- We need requests library to request data from the site
- We need to register at IMDB site to get an access token to be sent with this request
- Sample code to iterate through json objects in one line
`
[print('        ' + eachDir) for eachDir in [directorInfo['name'] + " " + directorInfo['description'] for directorInfo in movieCastData['directors']['items']]]
`
- In order to restrict number of rows/data from a list, use [:num] at the end. Code sample is below
`
 [print('        ' + eachDir) for eachDir in [directorInfo['name'] + " as " + directorInfo['asCharacter'] for directorInfo in movieCastData['actors'][:5]]]
`

I will keep on adding my notes as I go along
