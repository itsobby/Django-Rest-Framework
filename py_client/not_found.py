import requests

endpoint = "http://localhost:8000/api/products/38098498139/"

try:
    get_response = requests.get(endpoint)
    get_response.raise_for_status()  # Raise an exception if the response status code is not successful
    print(get_response.json())
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
