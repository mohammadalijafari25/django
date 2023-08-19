import requests
bestMovies =[]
for i in range(1,26):
    params = {
        "page" : i
    }
    #print(params)
    response = requests.get("http://moviesapi.ir/api/v1/movies",params = params)
    for i in range(0,10):
        print(response.json()["data"][i]['title'])
        bestMovies.append(response.json()["data"][i]['title'])

print(bestMovies)
print((len(bestMovies)))