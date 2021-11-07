import requests

url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

querystring = {"q":"get:new180:DE","p":"1","t":"ns","st":"adv"}

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "585bc4fb32msh9665ab728f61bbep1a8b86jsn8730d0d89a89"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)