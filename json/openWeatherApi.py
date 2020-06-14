import json, requests, sys

API_KEY = '792d505e7a9c3b263140201a5658b4fc'

if len(sys.argv) < 2:
    print(f'Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()

address = ''.join(sys.argv[1:])
url = f'https://api.openweathermap.org/data/2.5/forecast?q={address}&appid={API_KEY}'
response = requests.get(url)

response.raise_for_status()

weatherData = json.loads(response.text)

w = weatherData['list']
print(f'Current weather in {address}:')
print(w[0]["weather"][0]["main"], '-', w[1]['weather'][0]['description'])
print()
print('Tommorrow')
print(w[1]['weather'][0]['main'])
print()
print('Day after tommorrow')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
