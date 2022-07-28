import requests
from bs4 import BeautifulSoup

URL = "https://www.mashina.kg/search/all/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"

}


def get_html(url, params=''):                                       # возвращает html код этого сайта
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="list-item list-label")
    # print(items)
    cars = []
    for item in items:
        cars.append({
            "name": item.find("h2", class_='name').getText().strip(),
            "price": item.find("strong").getText().strip(),
            "characteristics1": item.find("p", class_='year-miles').getText().strip(),
            "characteristics2": item.find("p", class_='body-type').getText().strip(),
            "characteristics3": item.find("p", class_='volume').getText().strip(),
            "color": item.find('i', class_='color-icon').get('title'),
            "count_view": item.find('span').getText().strip(),
            'link': "https://www.mashina.kg" + item.find('a').get('href'),
        })
    # print(cars)
    return cars

# html = get_html(URL)
# get_data(html.text)


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = []
        for page in range(1, 2):
            html = get_html(f"{URL}page1_{page}.php")
            answer.extend(get_data(html.text))
        return answer
    else:
        raise Exception("Error in parser!")
