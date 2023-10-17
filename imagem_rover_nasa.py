import requests

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "guRCCl3bSbmdm0NGtq5CdXZh6jzxMSu2YG39e5WZ"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get(endpoint, params=query_params)
response

response.json()
photos = response.json()["photos"]
print(photos[4]["img_src"])         # Gera um link para uma imagem jpeg obtida conforme os parâmetros solicitados
print(photos[4]["camera"]["name"] ) # O nome da câmera que foi tirada a foto