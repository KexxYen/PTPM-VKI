import requests
import bs4

response = requests.get("https://sibdroid.ru/catalog/smartfony_samsung/")

# print(response.text)

bs = bs4.BeautifulSoup(response.text, 'html.parser')

phones = bs.find_all('div', class_='c20-body')

for phone in phones:
    name = phone.find('span', itemprop='name').text.strip()
    price = phone.find('span', itemprop='offers').text.strip()
    rate_check = phone.find('b')
    if rate_check:
        rate = rate_check.text.strip()
    else:
        rate = "нету"
    print(f"{name} - {price} - {rate}") 