movies = {}
import json, requests
url = "https://imdb-api.com/en/API/SearchMovie/k_d0rilf8k/"
with open("Movies.txt", "r") as fin:
     for line in fin:
         movieTitle = line.rstrip("\n") # get rid of newline characters
         response = requests.get(url + movieTitle)
         if response.status_code == 200:
              #movies[movieTitle] = json.loads(response.text)
              #movies[movieTitle] = json.loads(response)
              m = json.loads(response.text)
         else:
              raise ValueError("Bad request!")

for i in movies:
    print(i)