import requests

def unreleased_workshops():
    response = requests.get('https://codigofacilito.com/api/v2/workshops/unreleased')
    
    if response.status_code == 200:
        workshops = response.json().get('data')['workshops']
        return workshops
    
    return None