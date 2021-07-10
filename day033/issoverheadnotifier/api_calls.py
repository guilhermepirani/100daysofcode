import requests

def get_suntimes(lat, lng):
    response = requests.get('https://api.sunrise-sunset.org/json', params={'lat':lat, 'lng':lng, 'formatted':0})
    response.raise_for_status()
    suntimer = [response.json()['results'].get(key) for key in ['sunrise', 'sunset']]
    
    # spliting response to keep only hour values
    values = [item.split('T')[1].split(':')[0] for item in suntimer]
    return {'sunrise': values[0], 'sunset':values[1]}

def iss_position():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    return response.json()['iss_position']