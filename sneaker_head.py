import json
import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'sneakerhead.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru,en;q=0.9',
    'cookie': '_ga_cid=1638197206.1673529789; _ga_cid=1638197206.1673529789; BITRIX_SM_VIEWED_POSTS=%5B%5D; BITRIX_SM_sortRulesCode=date_avail_desc; tmr_lvid=f6b0789d89996ae5528c8891bb564811; tmr_lvidTS=1673529788922; _gcl_au=1.1.1813063691.1673529789; rrpvid=260470470317943; advcake_track_id=34378a40-e081-7711-db82-a5a75f2b3a5c; advcake_session_id=cf30e2b3-8d48-c577-d8a5-0c40fe7eb598; _gid=GA1.2.1499851388.1673529789; _ym_uid=1673529789456076694; _ym_d=1673529789; _userGUID=0:lct4fdli:tqmOua3qqOfYlz~xdWVeo9b7BmT4ibFU; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=e023806c-672d-45dd-b51f-56ea23de2850; rcuid=63c009c2523fdc7854ad65c6; BX_USER_ID=b1c1de5153b2028aa850a393c8a2c4fb; rraem=; analytic_id=1673529790497028; BITRIX_SM_SALE_UID=61bbeede18ff7b06b04bb2ef814226dd; rrtwdf=true; rrlevt=1673531333743; PHPSESSID=44e6d30cf4b9eeb4307aba8e6db4e0db; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A3%2C%22EXPIRE%22%3A1673643540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; dSesn=bf3e3d67-8a9c-fe33-f0de-1b9ed610ec82; _dvs=0:lcunyuex:dQlWi_2htwNqECsoby4qJF6DEDbwwtgT; _ym_visorc=w; _ym_isad=2; __cf_bm=dOXErmLSJW7eHsMnTnoqC4nmWpCNYCE0tDrrmCba7P8-1673623083-0-ASiwh+0dKmmPmw6cdaubkwQo1qd9ElMJo18U59Jbp1KTtGItP/FVcb7PBujX+cg6v3ira89OGGLXBVmMI2xmf3Rb7AaTLcEZay3YIq4EOHi8VsmMDtm1b2MXGzNHk323DuQluZhCgzFYqkwmvoHTobU=; _ga_cid=1638197206.1673529789; _dc_gtm_UA-22803482-1=1; _ga_FYE1HF13Q3=GS1.1.1673623076.5.1.1673623382.59.0.0; _ga=GA1.2.1638197206.1673529789; tmr_detect=0%7C1673623385300',
    'referer': 'https://sneakerhead.ru/sale/',
    'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
}


def sneaker_head_puma():
    response = requests.get('https://sneakerhead.ru/sale/puma/size-11-or-size-12/', headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    all_cards = soup.find_all("div", class_="product-cards__item")
    list = []
    for card in all_cards:
        url = card.find("a", class_="product-card__link").get("href")
        title = card.find("a", class_="product-card__link").text
        # old_price = card.find("span", class_="product-card__price-value product-card__price-value--old").text.replace("\n", "")
        price = int(card.find("span",
                              class_="product-card__price-value product-card__price-value--old").find_next().find_next().text.replace(
            "\n", "").replace(" ", "").replace("₽", "").strip())
        old_price = int(card.find("span",
                                  class_="product-card__price-value product-card__price-value--old").text.replace(
            "\n", "").replace("₽", "").strip().replace(" ", ""))
        dict = {"url": url, "title": title.strip(), "price": {
            "recommended": {
                "price": old_price
            },
            "special": {
                "price": price
            }}}
        list.append(dict)
    with open("sneakers.json", "w", encoding="utf-8") as file:
        json.dump(list, file, indent=4, ensure_ascii=False)
    return len(list)


def sneaker_head_adidas():
    response = requests.get('https://sneakerhead.ru/sale/shoes/sneakers/adidas-originals/size-11-or-size-11_5-or-size-12/', headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    all_cards = soup.find_all("div", class_="product-cards__item")
    list = []
    for card in all_cards:
        url = card.find("a", class_="product-card__link").get("href")
        title = card.find("a", class_="product-card__link").text
        price = int(card.find("span",
                              class_="product-card__price-value product-card__price-value--old").find_next().find_next().text.replace(
            "\n", "").replace(" ", "").replace("₽", "").strip())
        old_price = int(card.find("span",
                                  class_="product-card__price-value product-card__price-value--old").text.replace(
            "\n", "").replace("₽", "").strip().replace(" ", ""))
        dict = {"url": url, "title": title.strip(), "price": {
            "recommended": {
                "price": old_price
            },
            "special": {
                "price": price
            }}}
        list.append(dict)
    with open("sneakers.json", "w", encoding="utf-8") as file:
        json.dump(list, file, indent=4, ensure_ascii=False)
    return len(list)


def sneaker_head_new_balance():
    response = requests.get('https://sneakerhead.ru/sale/new-balance/size-11-or-size-12/', headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    all_cards = soup.find_all("div", class_="product-cards__item")
    list = []
    for card in all_cards:
        url = card.find("a", class_="product-card__link").get("href")
        title = card.find("a", class_="product-card__link").text
        price = int(card.find("span",
                              class_="product-card__price-value product-card__price-value--old").find_next().find_next().text.replace(
            "\n", "").replace(" ", "").replace("₽", "").strip())
        old_price = int(card.find("span",
                                  class_="product-card__price-value product-card__price-value--old").text.replace(
            "\n", "").replace("₽", "").strip().replace(" ", ""))
        dict = {"url": url, "title": title.strip(), "price": {
            "recommended": {
                "price": old_price
            },
            "special": {
                "price": price
            }}}
        list.append(dict)
    with open("sneakers.json", "w", encoding="utf-8") as file:
        json.dump(list, file, indent=4, ensure_ascii=False)
    return len(list)

def next_sneaker_head():
    with open("sneakers.json", "r", encoding="utf-8") as file:
        sneakers = json.load(file)
    list = [sneakers[0]]
    sneakers.remove(sneakers[0])
    with open("sneakers.json", "w", encoding="utf-8") as file:
        json.dump(sneakers, file, indent=4, ensure_ascii=False)

    for item in list:
        url = "https://sneakerhead.ru" + item["url"]
        title = item["title"]
        price = item["price"]["special"]["price"]
        sale = int((item["price"]["recommended"]["price"] - price) / item["price"]["recommended"]["price"] * 100)
        yield url, title, "Цена: " + str(price) + "RUB", "Скидка🔥 " + str(sale) + "%"


