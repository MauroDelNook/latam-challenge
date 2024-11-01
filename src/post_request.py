import requests

url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer"
data = {
    "name": "Mauricio Miranda",
    "mail": "mauricio_miranda@hotmail.com",
    "github_url": "https://github.com/MauroDelNook/latam-challenge.git"
}

response = requests.post(url, json=data)

# Chequear si estuvo correcto el envío
if response.status_code == 200:
    print("Request was successful!")
    print(response.json())  # Entrega respuesta del server si es en json
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)  # Mensaje de error