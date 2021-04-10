import requests


superheroes = {'Hulk': 0, 'Captain America': 0, 'Thanos': 0}
for superhero in superheroes.keys():
    http_request = "https://superheroapi.com/api/2619421814940190/search/" + superhero
    response = requests.get(http_request)
    json_response = response.json()
    superheroes[superhero] = [json_response['results'][0]['id'], int(json_response['results'][0]['powerstats']['intelligence'])]
most_intelligent = max(superheroes, key=lambda key: superheroes[key][1])
print('The most intelligent of superheroes is {}(id = {})'.format(most_intelligent, superheroes[most_intelligent][0]))