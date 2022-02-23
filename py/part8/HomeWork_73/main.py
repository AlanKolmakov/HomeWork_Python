from bs4 import BeautifulSoup
import csv
import requests
from datetime import date, timedelta

PAGES_COUNT = 10


def get_html(url, **kwargs):
    response = requests.get(url, **kwargs)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features='html.parser')
    else:
        soup = None
    return soup


def get_data(pages_count):
    urls = []
    count = 1
    dates = '10-dney'
    for page_n in range(pages_count):
        page_url = f"https://sinoptik.com.ru/pogoda/{city.lower()}/{dates}"
        dates = date.today() + timedelta(days=count)
        soup = get_html(page_url)
        if soup is None:
            break
        urls.append(page_url)
        print(page_url)
        count += 1
    return urls


def parse_weather(urls):
    for url in urls:
        soup = get_html(url)
        if soup is None:
            break
        if url == f"https://sinoptik.com.ru/pogoda/{city.lower()}/10-dney":
            dts = soup.find("a", class_="_3sAcyKeo U2Q5FSm6").get_text(strip=True, separator=" ")
            temp = soup.find("p", class_="_2LM4MsxZ").get_text(strip=True)
            description = soup.find("p", class_="_1w83DFg2").get_text(strip=True)
            item = {
                'Дата': dts,
                'Температура': temp,
                'Описание': description
            }
        else:
            dts = soup.find("div", class_="_2C2hfCsU").get_text(strip=True, separator=" ")
            temp = soup.find("tr", class_="OYAsiJbF _23BS_gTm").get_text(strip=True)
            description = soup.find("p", class_="_1w83DFg2").get_text(strip=True)
            item = {
                'Дата': dts,
                'Температура в течении дня': temp,
                'Описание': description
            }
        write_csv(item)


def write_csv(data_csv):
    with open("data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([data_csv])


def main():
    global city
    print("Пример: moskva, omsk, angarsk, default = irkutsk")
    city = input("Введите город (в англ. раскладке): ").lower().strip()
    if city == '':
        city = 'irkutsk'
    # with open('data.csv', "w") as f:
    #     pass
    urls = get_data(PAGES_COUNT)
    parse_weather(urls)
    # get_data(get_html(url))


if __name__ == "__main__":
    main()
