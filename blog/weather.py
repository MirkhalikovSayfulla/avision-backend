import requests
from bs4 import BeautifulSoup as BS


def get_weather(city: str) -> [str, str]:
    r = requests.get(f"https://sinoptik.ua/погода-{city}")
    html = BS(r.content, 'html.parser')
    el = html.select('#content')[0]
    temp = el.select('.temperature .max > span')[0].text
    weather_icon = el.select('.weatherIco')[0]
    return str(temp), str(weather_icon.get("title"))
