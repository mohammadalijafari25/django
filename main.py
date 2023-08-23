from requests import Session

sess = Session()

best_movies = []
for i in range(26):
    params = {
        "page" : i
    }
    #print(params)
    response = sess.get("http://moviesapi.ir/api/v1/movies", params = params)
    data = response.json()
    for item in data['data']:
        print(item['title'])
        best_movies.append(item['title'])

print(best_movies)
print((len(best_movies)))