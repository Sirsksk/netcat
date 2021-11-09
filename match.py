import requests

url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

querystring = {"q":"get-!1995,2021-!3,5-!0,10-!0-!Movie-!english-!english-!gt100-!{downloadable}","t":"ns","cl":"65,39","st":"adv","ob":"Relevance","p":"3","sa":"and"}

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': ""
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)