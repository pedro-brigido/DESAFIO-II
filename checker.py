import requests

def check_connectivity(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("O site está online.")
    except:
        print("O site está offline.")

# Exemplo de uso

check_connectivity("https://www.google.com/")
check_connectivity("https://www.udemy.com/")
check_connectivity("https://www.youtube.com/")
check_connectivity("www.netflix.com")