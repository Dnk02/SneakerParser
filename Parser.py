import json

import requests


def street_beat_adidas():
    json_data = {
        'filter': {
            'filters': [
                {
                    'key': 'GENDER',
                    'type': 'select',
                    'values': [
                        'man',
                        'unisex',
                    ],
                },
                {
                    'key': 'PRODUCT_STATUS',
                    'type': 'select',
                    'values': [
                        'sale',
                    ],
                },
                {
                    'key': 'BRAND',
                    'type': 'select',
                    'values': [
                        'adidas-originals',
                        'adidas-performance',
                    ]
                },
                {
                    'key': 'SIZE',
                    'type': 'group-size',
                    'selected': [
                        {
                            'code': 'SIZE',
                            'values': [
                                '44,5',
                                '45',
                                '45,5',
                                '46',
                            ],
                        },
                    ],
                },
                {
                    'key': 'SECTION_CODE',
                    'type': 'select-section',
                    'values': [
                        'obuv',
                    ],
                },
            ],
            'tags': [
                {
                    'type': 'filter',
                    'key': 'krossovki',
                    'title': 'Кроссовки',
                    'filters': [
                        {
                            'key': 'SECTION_CODE',
                            'type': 'select-section',
                            'values': [
                                'krossovki',
                            ],
                        },
                    ],
                },
            ],
        },
        'sorting': {
            'key': 'sort',
            'value': 'desc',
        },
        'seo': {
            'uri': '/cat/man/obuv/krossovki/sale/',
        }, }
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Cookie': 'rerf=AAAAAGO//255BLo7A026Ag==; ipp_uid=1673527149944/2KRGccKS3AuY3nhA/Y2ffoRNO0LRnWDko3z2uZQ==; __zzatinv-w-strbeat=MDA0dBA=Fz2+aQ==; BITRIX_SM_SALE_UID=1437421434; _gid=GA1.2.1903144150.1673527147; _ym_uid=167352714818532907; _ym_d=1673527148; tmr_lvid=2b7fffca76e5360c86b820d7007a4020; tmr_lvidTS=1673527148020; adrdel=1; adrcid=APZ0ZEJ53DFitHLX35fOcQw; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; user_city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; adspire_uid=AS.481304539.1673527149; atm_closer=%7B%22id%22%3A12690%2C%22mid%22%3A18509%2C%22aid%22%3A%22AS.481304539.1673527149%22%2C%22cookie_time%22%3A1673527149176%2C%22priority%22%3A0%7D; BX_USER_ID=d60081026a445bb3e98dc82c3b40ad89; _ym_isad=2; MgidSensorUtmSource=yandex; MgidSensorClidV=0; flomni_62f613edb13909b07c8e81ed={%22userHash%22:%2243ff27e5-b520-4d7e-b737-f18fddd1e680%22}; mainpagetype=man; user_usee=a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%223985606%22%3Bi%3A1%3Bs%3A7%3A%223864034%22%3B%7D; ipp_key=v1673554959424/v33947245ba5adc7a72e273/VwE4KpQeouKgRQSXF0MVsQ==; _ym_visorc=b; PHPSESSID=dTJFtPZDe5wIvf8dax1erw3tEqiCs5s7; topMenu_active=%2Fman%2F; gssc111=; _dc_gtm_UA-57250236-1=1; _ga_E3GN5VV3T0=GS1.1.1673554956.5.1.1673555561.0.0.0; MgidSensorNVis=56; MgidSensorHref=https://street-beat.ru/cat/man/sale/; _ga=GA1.2.359725046.1673527147; cfidsinv-w-strbeat=53TawzUgO0vAs/cgYm7po72+zJEvR1fl8XwaVk1b9heXGebL5XpPAotmu3oMG+85qXQzGWCZ3BE3ISox5QrIL4tBaTIhM/o5WiRW98xANNKVmSwY3DAIXJHj0wn5rWd1hI1sRZs3t68y5NxnV1WKP/ClNQ/B1ocbY/fbuA8=; cfidsinv-w-strbeat=53TawzUgO0vAs/cgYm7po72+zJEvR1fl8XwaVk1b9heXGebL5XpPAotmu3oMG+85qXQzGWCZ3BE3ISox5QrIL4tBaTIhM/o5WiRW98xANNKVmSwY3DAIXJHj0wn5rWd1hI1sRZs3t68y5NxnV1WKP/ClNQ/B1ocbY/fbuA8=; gsscinv-w-strbeat=93UW0d1e4ExJUHW8dL9lh3hxDN7lfQmZhTXV7soMPo8ZTzHl0ND+xEs9tDejaYWrDDPplYffmUQwgmNNZwx3jHsHdseTRyANeRYJ6kh9OnSbbEAPEuSLBhg8eG5v6O9D0ZJK2swx1Q4qdsBj2oiNiGuks+cJFJxamAUwubZuJQCmSeGrN1LHN1bct5eg0ilxdt80D3skdQJvyL+ugOt1JVYx0Ihg1vagXHcQrf45mTqITH+nDRxzMy94AFmXp+ojDsk=; mindboxDeviceUUID=401160c2-7b19-4196-b4be-f724465b04b1; directCrm-session=%7B%22deviceGuid%22%3A%22401160c2-7b19-4196-b4be-f724465b04b1%22%7D; tmr_detect=0%7C1673555564115; fgsscinv-w-strbeat=BQPO40dda538dec5b59b560d954ec768c5ed6807',
            'Origin': 'https://street-beat.ru',
            'Referer': 'https://street-beat.ru/cat/man/sale/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
            'X-GIB-FGSSCinv-w-strbeat': 'BQPO40dda538dec5b59b560d954ec768c5ed6807',
            'X-GIB-GSSCinv-w-strbeat': '93UW0d1e4ExJUHW8dL9lh3hxDN7lfQmZhTXV7soMPo8ZTzHl0ND+xEs9tDejaYWrDDPplYffmUQwgmNNZwx3jHsHdseTRyANeRYJ6kh9OnSbbEAPEuSLBhg8eG5v6O9D0ZJK2swx1Q4qdsBj2oiNiGuks+cJFJxamAUwubZuJQCmSeGrN1LHN1bct5eg0ilxdt80D3skdQJvyL+ugOt1JVYx0Ihg1vagXHcQrf45mTqITH+nDRxzMy94AFmXp+ojDsk=',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        session = requests.session()
        response = session.post("https://street-beat.ru/api/catalog/full", headers=headers, json=json_data)
        list = response.json()["catalog"]["listing"]["items"]
        with open("sneakers.json", "w", encoding="utf-8") as file:
            json.dump(list, file, indent=4, ensure_ascii=False)
        return len(list)
    except Exception:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Cookie': 'rerf=AAAAAGO//255BLo7A026Ag==; ipp_uid=1673527149944/2KRGccKS3AuY3nhA/Y2ffoRNO0LRnWDko3z2uZQ==; __zzatinv-w-strbeat=MDA0dBA=Fz2+aQ==; BITRIX_SM_SALE_UID=1437421434; _gid=GA1.2.1903144150.1673527147; _ym_uid=167352714818532907; _ym_d=1673527148; tmr_lvid=2b7fffca76e5360c86b820d7007a4020; tmr_lvidTS=1673527148020; adrcid=APZ0ZEJ53DFitHLX35fOcQw; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; user_city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; adspire_uid=AS.481304539.1673527149; atm_closer=%7B%22id%22%3A12690%2C%22mid%22%3A18509%2C%22aid%22%3A%22AS.481304539.1673527149%22%2C%22cookie_time%22%3A1673527149176%2C%22priority%22%3A0%7D; BX_USER_ID=d60081026a445bb3e98dc82c3b40ad89; MgidSensorUtmSource=yandex; MgidSensorClidV=0; flomni_62f613edb13909b07c8e81ed={%22userHash%22:%2243ff27e5-b520-4d7e-b737-f18fddd1e680%22}; mainpagetype=man; user_usee=a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%223985606%22%3Bi%3A1%3Bs%3A7%3A%223864034%22%3B%7D; PHPSESSID=Y6Jo9nfKLnaB9syFz1HOfr6VCkV7VOtp; ipp_key=v1673612112928/v33947245ba5adc7a72e273/Iu6urgN0+qErQgYXQ0NBgg==; topMenu_active=%2Fman%2F; _dc_gtm_UA-57250236-1=1; _ym_isad=2; _ym_visorc=w; _ga=GA1.2.359725046.1673527147; MgidSensorNVis=61; MgidSensorHref=https://street-beat.ru/cat/man/obuv/sale/; cfidsinv-w-strbeat=e5+G4yyKJI/lqzQBU/p+JywZPDDyHM4Wt852oHZzz23rK11QgbGkG7Am3VA2erDPug3mnqPcdvM22UTRzE3HMnqTZ5dTefuS4LJivZLGygBwuHjAUm6nbzjTn3rhmS1HI+anXwIdTpIWFHBf8uE6zDTejmVycM03jx2mVwQ=; cfidsinv-w-strbeat=e5+G4yyKJI/lqzQBU/p+JywZPDDyHM4Wt852oHZzz23rK11QgbGkG7Am3VA2erDPug3mnqPcdvM22UTRzE3HMnqTZ5dTefuS4LJivZLGygBwuHjAUm6nbzjTn3rhmS1HI+anXwIdTpIWFHBf8uE6zDTejmVycM03jx2mVwQ=; gsscinv-w-strbeat=eGK6OwygecZqQB5d3TMT1UTGusf5jq0O41m+5RcxID/2NQayHjSAbDdnq/YxkF9zuF630izQfcUoW9iqtC0ejnrRYLjbRMNFTrJjzJR0HtNQcVUBL+uh8vWX744l93ObouJoZUqsZJzbUKuLyhdwielzJluw/J9hnb0kpW45njcbkYfUtRasnKpfdb3qt9NuymlbnIiHmFquBmV9VkFQ8AOVYUWToaQItlbNl+bLxcPm2O2R2gw/eX3bnbwtv5TY39g=; tmr_detect=0%7C1673612148281; _ga_E3GN5VV3T0=GS1.1.1673612110.6.1.1673612155.0.0.0; mindboxDeviceUUID=401160c2-7b19-4196-b4be-f724465b04b1; directCrm-session=%7B%22deviceGuid%22%3A%22401160c2-7b19-4196-b4be-f724465b04b1%22%7D; fgsscinv-w-strbeat=CLDFf1bc5d4006aafe0a7b3fac5a40cdd5a2fdfc',
            'Origin': 'https://street-beat.ru',
            'Referer': 'https://street-beat.ru/cat/man/obuv/krossovki/adidas-originals/sale/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
            'X-GIB-FGSSCinv-w-strbeat': 'CLDFf1bc5d4006aafe0a7b3fac5a40cdd5a2fdfc',
            'X-GIB-GSSCinv-w-strbeat': 'eGK6OwygecZqQB5d3TMT1UTGusf5jq0O41m+5RcxID/2NQayHjSAbDdnq/YxkF9zuF630izQfcUoW9iqtC0ejnrRYLjbRMNFTrJjzJR0HtNQcVUBL+uh8vWX744l93ObouJoZUqsZJzbUKuLyhdwielzJluw/J9hnb0kpW45njcbkYfUtRasnKpfdb3qt9NuymlbnIiHmFquBmV9VkFQ8AOVYUWToaQItlbNl+bLxcPm2O2R2gw/eX3bnbwtv5TY39g=',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        session = requests.session()
        response = session.post("https://street-beat.ru/api/catalog/full", headers=headers, json=json_data)
        list = response.json()["catalog"]["listing"]["items"]
        with open("sneakers.json", "w", encoding="utf-8") as file:
            json.dump(list, file, indent=4, ensure_ascii=False)
        return len(list)


def street_beat_reebok():
    json_data = {
        'filter': {
            'filters': [
                {
                    'key': 'GENDER',
                    'type': 'select',
                    'values': [
                        'man',
                        'unisex',
                    ],
                },
                {
                    'key': 'PRODUCT_STATUS',
                    'type': 'select',
                    'values': [
                        'sale',
                    ],
                },
                {
                    'key': 'BRAND',
                    'type': 'select',
                    'values': [
                        'reebok',
                    ]
                },
                {
                    'key': 'SIZE',
                    'type': 'group-size',
                    'selected': [
                        {
                            'code': 'SIZE',
                            'values': [
                                '44,5',
                                '45',
                                '45,5',
                                '46',
                            ],
                        },
                    ],
                },
                {
                    'key': 'SECTION_CODE',
                    'type': 'select-section',
                    'values': [
                        'obuv',
                    ],
                },
            ],
            'tags': [
                {
                    'type': 'filter',
                    'key': 'krossovki',
                    'title': 'Кроссовки',
                    'filters': [
                        {
                            'key': 'SECTION_CODE',
                            'type': 'select-section',
                            'values': [
                                'krossovki',
                            ],
                        },
                    ],
                },
            ],
        },
        'sorting': {
            'key': 'sort',
            'value': 'desc',
        },
        'seo': {
            'uri': '/cat/man/obuv/krossovki/sale/',
        }, }
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Cookie': 'rerf=AAAAAGO//255BLo7A026Ag==; ipp_uid=1673527149944/2KRGccKS3AuY3nhA/Y2ffoRNO0LRnWDko3z2uZQ==; __zzatinv-w-strbeat=MDA0dBA=Fz2+aQ==; BITRIX_SM_SALE_UID=1437421434; _gid=GA1.2.1903144150.1673527147; _ym_uid=167352714818532907; _ym_d=1673527148; tmr_lvid=2b7fffca76e5360c86b820d7007a4020; tmr_lvidTS=1673527148020; adrdel=1; adrcid=APZ0ZEJ53DFitHLX35fOcQw; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; user_city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; adspire_uid=AS.481304539.1673527149; atm_closer=%7B%22id%22%3A12690%2C%22mid%22%3A18509%2C%22aid%22%3A%22AS.481304539.1673527149%22%2C%22cookie_time%22%3A1673527149176%2C%22priority%22%3A0%7D; BX_USER_ID=d60081026a445bb3e98dc82c3b40ad89; _ym_isad=2; MgidSensorUtmSource=yandex; MgidSensorClidV=0; flomni_62f613edb13909b07c8e81ed={%22userHash%22:%2243ff27e5-b520-4d7e-b737-f18fddd1e680%22}; mainpagetype=man; user_usee=a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%223985606%22%3Bi%3A1%3Bs%3A7%3A%223864034%22%3B%7D; ipp_key=v1673554959424/v33947245ba5adc7a72e273/VwE4KpQeouKgRQSXF0MVsQ==; _ym_visorc=b; PHPSESSID=dTJFtPZDe5wIvf8dax1erw3tEqiCs5s7; topMenu_active=%2Fman%2F; gssc111=; _dc_gtm_UA-57250236-1=1; _ga_E3GN5VV3T0=GS1.1.1673554956.5.1.1673555561.0.0.0; MgidSensorNVis=56; MgidSensorHref=https://street-beat.ru/cat/man/sale/; _ga=GA1.2.359725046.1673527147; cfidsinv-w-strbeat=53TawzUgO0vAs/cgYm7po72+zJEvR1fl8XwaVk1b9heXGebL5XpPAotmu3oMG+85qXQzGWCZ3BE3ISox5QrIL4tBaTIhM/o5WiRW98xANNKVmSwY3DAIXJHj0wn5rWd1hI1sRZs3t68y5NxnV1WKP/ClNQ/B1ocbY/fbuA8=; cfidsinv-w-strbeat=53TawzUgO0vAs/cgYm7po72+zJEvR1fl8XwaVk1b9heXGebL5XpPAotmu3oMG+85qXQzGWCZ3BE3ISox5QrIL4tBaTIhM/o5WiRW98xANNKVmSwY3DAIXJHj0wn5rWd1hI1sRZs3t68y5NxnV1WKP/ClNQ/B1ocbY/fbuA8=; gsscinv-w-strbeat=93UW0d1e4ExJUHW8dL9lh3hxDN7lfQmZhTXV7soMPo8ZTzHl0ND+xEs9tDejaYWrDDPplYffmUQwgmNNZwx3jHsHdseTRyANeRYJ6kh9OnSbbEAPEuSLBhg8eG5v6O9D0ZJK2swx1Q4qdsBj2oiNiGuks+cJFJxamAUwubZuJQCmSeGrN1LHN1bct5eg0ilxdt80D3skdQJvyL+ugOt1JVYx0Ihg1vagXHcQrf45mTqITH+nDRxzMy94AFmXp+ojDsk=; mindboxDeviceUUID=401160c2-7b19-4196-b4be-f724465b04b1; directCrm-session=%7B%22deviceGuid%22%3A%22401160c2-7b19-4196-b4be-f724465b04b1%22%7D; tmr_detect=0%7C1673555564115; fgsscinv-w-strbeat=BQPO40dda538dec5b59b560d954ec768c5ed6807',
            'Origin': 'https://street-beat.ru',
            'Referer': 'https://street-beat.ru/cat/man/sale/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
            'X-GIB-FGSSCinv-w-strbeat': 'BQPO40dda538dec5b59b560d954ec768c5ed6807',
            'X-GIB-GSSCinv-w-strbeat': '93UW0d1e4ExJUHW8dL9lh3hxDN7lfQmZhTXV7soMPo8ZTzHl0ND+xEs9tDejaYWrDDPplYffmUQwgmNNZwx3jHsHdseTRyANeRYJ6kh9OnSbbEAPEuSLBhg8eG5v6O9D0ZJK2swx1Q4qdsBj2oiNiGuks+cJFJxamAUwubZuJQCmSeGrN1LHN1bct5eg0ilxdt80D3skdQJvyL+ugOt1JVYx0Ihg1vagXHcQrf45mTqITH+nDRxzMy94AFmXp+ojDsk=',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        session = requests.session()
        response = session.post("https://street-beat.ru/api/catalog/full", headers=headers, json=json_data)
        list = response.json()["catalog"]["listing"]["items"]
        with open("sneakers.json", "w", encoding="utf-8") as file:
            json.dump(list, file, indent=4, ensure_ascii=False)
        return len(list)
    except Exception:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Cookie': 'rerf=AAAAAGO//255BLo7A026Ag==; ipp_uid=1673527149944/2KRGccKS3AuY3nhA/Y2ffoRNO0LRnWDko3z2uZQ==; __zzatinv-w-strbeat=MDA0dBA=Fz2+aQ==; BITRIX_SM_SALE_UID=1437421434; _gid=GA1.2.1903144150.1673527147; _ym_uid=167352714818532907; _ym_d=1673527148; tmr_lvid=2b7fffca76e5360c86b820d7007a4020; tmr_lvidTS=1673527148020; adrcid=APZ0ZEJ53DFitHLX35fOcQw; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; user_city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; adspire_uid=AS.481304539.1673527149; atm_closer=%7B%22id%22%3A12690%2C%22mid%22%3A18509%2C%22aid%22%3A%22AS.481304539.1673527149%22%2C%22cookie_time%22%3A1673527149176%2C%22priority%22%3A0%7D; BX_USER_ID=d60081026a445bb3e98dc82c3b40ad89; MgidSensorUtmSource=yandex; MgidSensorClidV=0; flomni_62f613edb13909b07c8e81ed={%22userHash%22:%2243ff27e5-b520-4d7e-b737-f18fddd1e680%22}; mainpagetype=man; user_usee=a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%223985606%22%3Bi%3A1%3Bs%3A7%3A%223864034%22%3B%7D; PHPSESSID=Y6Jo9nfKLnaB9syFz1HOfr6VCkV7VOtp; ipp_key=v1673612112928/v33947245ba5adc7a72e273/Iu6urgN0+qErQgYXQ0NBgg==; topMenu_active=%2Fman%2F; _dc_gtm_UA-57250236-1=1; _ym_isad=2; _ym_visorc=w; _ga=GA1.2.359725046.1673527147; MgidSensorNVis=61; MgidSensorHref=https://street-beat.ru/cat/man/obuv/sale/; cfidsinv-w-strbeat=e5+G4yyKJI/lqzQBU/p+JywZPDDyHM4Wt852oHZzz23rK11QgbGkG7Am3VA2erDPug3mnqPcdvM22UTRzE3HMnqTZ5dTefuS4LJivZLGygBwuHjAUm6nbzjTn3rhmS1HI+anXwIdTpIWFHBf8uE6zDTejmVycM03jx2mVwQ=; cfidsinv-w-strbeat=e5+G4yyKJI/lqzQBU/p+JywZPDDyHM4Wt852oHZzz23rK11QgbGkG7Am3VA2erDPug3mnqPcdvM22UTRzE3HMnqTZ5dTefuS4LJivZLGygBwuHjAUm6nbzjTn3rhmS1HI+anXwIdTpIWFHBf8uE6zDTejmVycM03jx2mVwQ=; gsscinv-w-strbeat=eGK6OwygecZqQB5d3TMT1UTGusf5jq0O41m+5RcxID/2NQayHjSAbDdnq/YxkF9zuF630izQfcUoW9iqtC0ejnrRYLjbRMNFTrJjzJR0HtNQcVUBL+uh8vWX744l93ObouJoZUqsZJzbUKuLyhdwielzJluw/J9hnb0kpW45njcbkYfUtRasnKpfdb3qt9NuymlbnIiHmFquBmV9VkFQ8AOVYUWToaQItlbNl+bLxcPm2O2R2gw/eX3bnbwtv5TY39g=; tmr_detect=0%7C1673612148281; _ga_E3GN5VV3T0=GS1.1.1673612110.6.1.1673612155.0.0.0; mindboxDeviceUUID=401160c2-7b19-4196-b4be-f724465b04b1; directCrm-session=%7B%22deviceGuid%22%3A%22401160c2-7b19-4196-b4be-f724465b04b1%22%7D; fgsscinv-w-strbeat=CLDFf1bc5d4006aafe0a7b3fac5a40cdd5a2fdfc',
            'Origin': 'https://street-beat.ru',
            'Referer': 'https://street-beat.ru/cat/man/obuv/krossovki/adidas-originals/sale/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
            'X-GIB-FGSSCinv-w-strbeat': 'CLDFf1bc5d4006aafe0a7b3fac5a40cdd5a2fdfc',
            'X-GIB-GSSCinv-w-strbeat': 'eGK6OwygecZqQB5d3TMT1UTGusf5jq0O41m+5RcxID/2NQayHjSAbDdnq/YxkF9zuF630izQfcUoW9iqtC0ejnrRYLjbRMNFTrJjzJR0HtNQcVUBL+uh8vWX744l93ObouJoZUqsZJzbUKuLyhdwielzJluw/J9hnb0kpW45njcbkYfUtRasnKpfdb3qt9NuymlbnIiHmFquBmV9VkFQ8AOVYUWToaQItlbNl+bLxcPm2O2R2gw/eX3bnbwtv5TY39g=',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        session = requests.session()
        response = session.post("https://street-beat.ru/api/catalog/full", headers=headers, json=json_data)
        list = response.json()["catalog"]["listing"]["items"]
        with open("sneakers.json", "w", encoding="utf-8") as file:
            json.dump(list, file, indent=4, ensure_ascii=False)
        return len(list)


def street_beat_new_balance():
    json_data = {
        'filter': {
            'filters': [
                {
                    'key': 'GENDER',
                    'type': 'select',
                    'values': [
                        'man',
                        'unisex',
                    ],
                },
                {
                    'key': 'PRODUCT_STATUS',
                    'type': 'select',
                    'values': [
                        'sale',
                    ],
                },
                {
                    'key': 'BRAND',
                    'type': 'select',
                    'values': [
                        'new_balance',
                    ]
                },
                {
                    'key': 'SIZE',
                    'type': 'group-size',
                    'selected': [
                        {
                            'code': 'SIZE',
                            'values': [
                                '44,5',
                                '45',
                                '45,5',
                                '46',
                            ],
                        },
                    ],
                },
                {
                    'key': 'SECTION_CODE',
                    'type': 'select-section',
                    'values': [
                        'obuv',
                    ],
                },
            ],
            'tags': [
                {
                    'type': 'filter',
                    'key': 'krossovki',
                    'title': 'Кроссовки',
                    'filters': [
                        {
                            'key': 'SECTION_CODE',
                            'type': 'select-section',
                            'values': [
                                'krossovki',
                            ],
                        },
                    ],
                },
            ],
        },
        'sorting': {
            'key': 'sort',
            'value': 'desc',
        },
        'seo': {
            'uri': '/cat/man/obuv/krossovki/sale/',
        }, }
    try:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Cookie': 'rerf=AAAAAGO//255BLo7A026Ag==; ipp_uid=1673527149944/2KRGccKS3AuY3nhA/Y2ffoRNO0LRnWDko3z2uZQ==; __zzatinv-w-strbeat=MDA0dBA=Fz2+aQ==; BITRIX_SM_SALE_UID=1437421434; _gid=GA1.2.1903144150.1673527147; _ym_uid=167352714818532907; _ym_d=1673527148; tmr_lvid=2b7fffca76e5360c86b820d7007a4020; tmr_lvidTS=1673527148020; adrdel=1; adrcid=APZ0ZEJ53DFitHLX35fOcQw; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; user_city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; adspire_uid=AS.481304539.1673527149; atm_closer=%7B%22id%22%3A12690%2C%22mid%22%3A18509%2C%22aid%22%3A%22AS.481304539.1673527149%22%2C%22cookie_time%22%3A1673527149176%2C%22priority%22%3A0%7D; BX_USER_ID=d60081026a445bb3e98dc82c3b40ad89; _ym_isad=2; MgidSensorUtmSource=yandex; MgidSensorClidV=0; flomni_62f613edb13909b07c8e81ed={%22userHash%22:%2243ff27e5-b520-4d7e-b737-f18fddd1e680%22}; mainpagetype=man; user_usee=a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%223985606%22%3Bi%3A1%3Bs%3A7%3A%223864034%22%3B%7D; ipp_key=v1673554959424/v33947245ba5adc7a72e273/VwE4KpQeouKgRQSXF0MVsQ==; _ym_visorc=b; PHPSESSID=dTJFtPZDe5wIvf8dax1erw3tEqiCs5s7; topMenu_active=%2Fman%2F; gssc111=; _dc_gtm_UA-57250236-1=1; _ga_E3GN5VV3T0=GS1.1.1673554956.5.1.1673555561.0.0.0; MgidSensorNVis=56; MgidSensorHref=https://street-beat.ru/cat/man/sale/; _ga=GA1.2.359725046.1673527147; cfidsinv-w-strbeat=53TawzUgO0vAs/cgYm7po72+zJEvR1fl8XwaVk1b9heXGebL5XpPAotmu3oMG+85qXQzGWCZ3BE3ISox5QrIL4tBaTIhM/o5WiRW98xANNKVmSwY3DAIXJHj0wn5rWd1hI1sRZs3t68y5NxnV1WKP/ClNQ/B1ocbY/fbuA8=; cfidsinv-w-strbeat=53TawzUgO0vAs/cgYm7po72+zJEvR1fl8XwaVk1b9heXGebL5XpPAotmu3oMG+85qXQzGWCZ3BE3ISox5QrIL4tBaTIhM/o5WiRW98xANNKVmSwY3DAIXJHj0wn5rWd1hI1sRZs3t68y5NxnV1WKP/ClNQ/B1ocbY/fbuA8=; gsscinv-w-strbeat=93UW0d1e4ExJUHW8dL9lh3hxDN7lfQmZhTXV7soMPo8ZTzHl0ND+xEs9tDejaYWrDDPplYffmUQwgmNNZwx3jHsHdseTRyANeRYJ6kh9OnSbbEAPEuSLBhg8eG5v6O9D0ZJK2swx1Q4qdsBj2oiNiGuks+cJFJxamAUwubZuJQCmSeGrN1LHN1bct5eg0ilxdt80D3skdQJvyL+ugOt1JVYx0Ihg1vagXHcQrf45mTqITH+nDRxzMy94AFmXp+ojDsk=; mindboxDeviceUUID=401160c2-7b19-4196-b4be-f724465b04b1; directCrm-session=%7B%22deviceGuid%22%3A%22401160c2-7b19-4196-b4be-f724465b04b1%22%7D; tmr_detect=0%7C1673555564115; fgsscinv-w-strbeat=BQPO40dda538dec5b59b560d954ec768c5ed6807',
            'Origin': 'https://street-beat.ru',
            'Referer': 'https://street-beat.ru/cat/man/sale/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
            'X-GIB-FGSSCinv-w-strbeat': 'BQPO40dda538dec5b59b560d954ec768c5ed6807',
            'X-GIB-GSSCinv-w-strbeat': '93UW0d1e4ExJUHW8dL9lh3hxDN7lfQmZhTXV7soMPo8ZTzHl0ND+xEs9tDejaYWrDDPplYffmUQwgmNNZwx3jHsHdseTRyANeRYJ6kh9OnSbbEAPEuSLBhg8eG5v6O9D0ZJK2swx1Q4qdsBj2oiNiGuks+cJFJxamAUwubZuJQCmSeGrN1LHN1bct5eg0ilxdt80D3skdQJvyL+ugOt1JVYx0Ihg1vagXHcQrf45mTqITH+nDRxzMy94AFmXp+ojDsk=',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        session = requests.session()
        response = session.post("https://street-beat.ru/api/catalog/full", headers=headers, json=json_data)
        list = response.json()["catalog"]["listing"]["items"]
        with open("sneakers.json", "w", encoding="utf-8") as file:
            json.dump(list, file, indent=4, ensure_ascii=False)
        return len(list)
    except Exception:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Cookie': 'rerf=AAAAAGO//255BLo7A026Ag==; ipp_uid=1673527149944/2KRGccKS3AuY3nhA/Y2ffoRNO0LRnWDko3z2uZQ==; __zzatinv-w-strbeat=MDA0dBA=Fz2+aQ==; BITRIX_SM_SALE_UID=1437421434; _gid=GA1.2.1903144150.1673527147; _ym_uid=167352714818532907; _ym_d=1673527148; tmr_lvid=2b7fffca76e5360c86b820d7007a4020; tmr_lvidTS=1673527148020; adrcid=APZ0ZEJ53DFitHLX35fOcQw; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; user_city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; adspire_uid=AS.481304539.1673527149; atm_closer=%7B%22id%22%3A12690%2C%22mid%22%3A18509%2C%22aid%22%3A%22AS.481304539.1673527149%22%2C%22cookie_time%22%3A1673527149176%2C%22priority%22%3A0%7D; BX_USER_ID=d60081026a445bb3e98dc82c3b40ad89; MgidSensorUtmSource=yandex; MgidSensorClidV=0; flomni_62f613edb13909b07c8e81ed={%22userHash%22:%2243ff27e5-b520-4d7e-b737-f18fddd1e680%22}; mainpagetype=man; user_usee=a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%223985606%22%3Bi%3A1%3Bs%3A7%3A%223864034%22%3B%7D; PHPSESSID=Y6Jo9nfKLnaB9syFz1HOfr6VCkV7VOtp; ipp_key=v1673612112928/v33947245ba5adc7a72e273/Iu6urgN0+qErQgYXQ0NBgg==; topMenu_active=%2Fman%2F; _dc_gtm_UA-57250236-1=1; _ym_isad=2; _ym_visorc=w; _ga=GA1.2.359725046.1673527147; MgidSensorNVis=61; MgidSensorHref=https://street-beat.ru/cat/man/obuv/sale/; cfidsinv-w-strbeat=e5+G4yyKJI/lqzQBU/p+JywZPDDyHM4Wt852oHZzz23rK11QgbGkG7Am3VA2erDPug3mnqPcdvM22UTRzE3HMnqTZ5dTefuS4LJivZLGygBwuHjAUm6nbzjTn3rhmS1HI+anXwIdTpIWFHBf8uE6zDTejmVycM03jx2mVwQ=; cfidsinv-w-strbeat=e5+G4yyKJI/lqzQBU/p+JywZPDDyHM4Wt852oHZzz23rK11QgbGkG7Am3VA2erDPug3mnqPcdvM22UTRzE3HMnqTZ5dTefuS4LJivZLGygBwuHjAUm6nbzjTn3rhmS1HI+anXwIdTpIWFHBf8uE6zDTejmVycM03jx2mVwQ=; gsscinv-w-strbeat=eGK6OwygecZqQB5d3TMT1UTGusf5jq0O41m+5RcxID/2NQayHjSAbDdnq/YxkF9zuF630izQfcUoW9iqtC0ejnrRYLjbRMNFTrJjzJR0HtNQcVUBL+uh8vWX744l93ObouJoZUqsZJzbUKuLyhdwielzJluw/J9hnb0kpW45njcbkYfUtRasnKpfdb3qt9NuymlbnIiHmFquBmV9VkFQ8AOVYUWToaQItlbNl+bLxcPm2O2R2gw/eX3bnbwtv5TY39g=; tmr_detect=0%7C1673612148281; _ga_E3GN5VV3T0=GS1.1.1673612110.6.1.1673612155.0.0.0; mindboxDeviceUUID=401160c2-7b19-4196-b4be-f724465b04b1; directCrm-session=%7B%22deviceGuid%22%3A%22401160c2-7b19-4196-b4be-f724465b04b1%22%7D; fgsscinv-w-strbeat=CLDFf1bc5d4006aafe0a7b3fac5a40cdd5a2fdfc',
            'Origin': 'https://street-beat.ru',
            'Referer': 'https://street-beat.ru/cat/man/obuv/krossovki/adidas-originals/sale/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
            'X-GIB-FGSSCinv-w-strbeat': 'CLDFf1bc5d4006aafe0a7b3fac5a40cdd5a2fdfc',
            'X-GIB-GSSCinv-w-strbeat': 'eGK6OwygecZqQB5d3TMT1UTGusf5jq0O41m+5RcxID/2NQayHjSAbDdnq/YxkF9zuF630izQfcUoW9iqtC0ejnrRYLjbRMNFTrJjzJR0HtNQcVUBL+uh8vWX744l93ObouJoZUqsZJzbUKuLyhdwielzJluw/J9hnb0kpW45njcbkYfUtRasnKpfdb3qt9NuymlbnIiHmFquBmV9VkFQ8AOVYUWToaQItlbNl+bLxcPm2O2R2gw/eX3bnbwtv5TY39g=',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        session = requests.session()
        response = session.post("https://street-beat.ru/api/catalog/full", headers=headers, json=json_data)
        list = response.json()["catalog"]["listing"]["items"]
        with open("sneakers.json", "w", encoding="utf-8") as file:
            json.dump(list, file, indent=4, ensure_ascii=False)
        return len(list)


def street_beat_puma():
    json_data = {
        'filter': {
            'filters': [
                {
                    'key': 'GENDER',
                    'type': 'select',
                    'values': [
                        'man',
                        'unisex',
                    ],
                },
                {
                    'key': 'PRODUCT_STATUS',
                    'type': 'select',
                    'values': [
                        'sale',
                    ],
                },
                {
                    'key': 'BRAND',
                    'type': 'select',
                    'values': [
                        'puma',
                    ],
                },
                {
                    'key': 'SIZE',
                    'type': 'group-size',
                    'selected': [
                        {
                            'code': 'SIZE',
                            'values': [
                                '44,5',
                                '45',
                                '45,5',
                                '46',
                            ],
                        },
                    ],
                },
                {
                    'key': 'SECTION_CODE',
                    'type': 'select-section',
                    'values': [
                        'obuv',
                    ],
                },
            ],
            'tags': [
                {
                    'type': 'filter',
                    'key': 'krossovki',
                    'title': 'Кроссовки',
                    'filters': [
                        {
                            'key': 'SECTION_CODE',
                            'type': 'select-section',
                            'values': [
                                'krossovki',
                            ],
                        },
                    ],
                },
            ],
        },
        'sorting': {
            'key': 'sort',
            'value': 'desc',
        },
        'seo': {
            'uri': '/cat/man/obuv/krossovki/sale/',
        }, }
    try:
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Cookie': 'rerf=AAAAAGO//255BLo7A026Ag==; ipp_uid=1673527149944/2KRGccKS3AuY3nhA/Y2ffoRNO0LRnWDko3z2uZQ==; __zzatinv-w-strbeat=MDA0dBA=Fz2+aQ==; BITRIX_SM_SALE_UID=1437421434; _gid=GA1.2.1903144150.1673527147; _ym_uid=167352714818532907; _ym_d=1673527148; tmr_lvid=2b7fffca76e5360c86b820d7007a4020; tmr_lvidTS=1673527148020; adrcid=APZ0ZEJ53DFitHLX35fOcQw; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; user_city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; adspire_uid=AS.481304539.1673527149; atm_closer=%7B%22id%22%3A12690%2C%22mid%22%3A18509%2C%22aid%22%3A%22AS.481304539.1673527149%22%2C%22cookie_time%22%3A1673527149176%2C%22priority%22%3A0%7D; BX_USER_ID=d60081026a445bb3e98dc82c3b40ad89; MgidSensorUtmSource=yandex; MgidSensorClidV=0; flomni_62f613edb13909b07c8e81ed={%22userHash%22:%2243ff27e5-b520-4d7e-b737-f18fddd1e680%22}; mainpagetype=man; user_usee=a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%223985606%22%3Bi%3A1%3Bs%3A7%3A%223864034%22%3B%7D; _ym_isad=2; PHPSESSID=ZMq8nGsYEJ5XObIkgd1214a1raRQXLN6; ipp_key=v1673616859052/v33947245ba5adc7a72e273//ePRbIb+cQRu/R5VU1UvZQ==; _dc_gtm_UA-57250236-1=1; _ym_visorc=w; gssc111=; topMenu_active=%2Fman%2F; tmr_detect=0%7C1673616869275; MgidSensorNVis=64; MgidSensorHref=https://street-beat.ru/cat/man/sale/; gsscinv-w-strbeat=EEEVVlq4YCG/hrg6N5KJamTKNWU/NB5DsOivpa8LRIE/xWIXBVgWF1XvTDR0wOKbw2pddr3uWnj/+gQABn47oakoo/x+DjBwnC+3RD/pBp3tZiwaku5V9qDWYfF27XZUHCR0GfZMS7qlIykjo8w2bjDMkVnV6rL6Grs0ylCUmKULe6ZhuDvUvj+7e66VeISKQYd9Ho6VFFzG7+p7jwgGVHp8Gxy+s0LkcdvqEP7a5eUUTOX+O3C2RQfLzpw31Ro7pNo=; mindboxDeviceUUID=401160c2-7b19-4196-b4be-f724465b04b1; directCrm-session=%7B%22deviceGuid%22%3A%22401160c2-7b19-4196-b4be-f724465b04b1%22%7D; cfidsinv-w-strbeat=aSPPprt0l4rFzAwNTaVqPdKbU5fzUU9n4YCE3QpKgsRUaYNFIPJ85eVP3e6d9NjeE24nifDHQlUa0GrcZkMepChRoUfjmG9EqavrZ9ApQ7PyxtFIq91LTF6FlW0IAL5GzxqYRIcFPacYy3ajw/1XXJJ9LJ3/Q4d1eJT9OR4=; cfidsinv-w-strbeat=aSPPprt0l4rFzAwNTaVqPdKbU5fzUU9n4YCE3QpKgsRUaYNFIPJ85eVP3e6d9NjeE24nifDHQlUa0GrcZkMepChRoUfjmG9EqavrZ9ApQ7PyxtFIq91LTF6FlW0IAL5GzxqYRIcFPacYy3ajw/1XXJJ9LJ3/Q4d1eJT9OR4=; _ga_E3GN5VV3T0=GS1.1.1673616854.7.1.1673616882.0.0.0; _ga=GA1.1.359725046.1673527147; fgsscinv-w-strbeat=3LIZcee758866b28886b8f0ba5c00d332b06e165',
            'Origin': 'https://street-beat.ru',
            'Referer': 'https://street-beat.ru/cat/man/obuv/sale/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
            'X-GIB-FGSSCinv-w-strbeat': '3LIZcee758866b28886b8f0ba5c00d332b06e165',
            'X-GIB-GSSCinv-w-strbeat': 'EEEVVlq4YCG/hrg6N5KJamTKNWU/NB5DsOivpa8LRIE/xWIXBVgWF1XvTDR0wOKbw2pddr3uWnj/+gQABn47oakoo/x+DjBwnC+3RD/pBp3tZiwaku5V9qDWYfF27XZUHCR0GfZMS7qlIykjo8w2bjDMkVnV6rL6Grs0ylCUmKULe6ZhuDvUvj+7e66VeISKQYd9Ho6VFFzG7+p7jwgGVHp8Gxy+s0LkcdvqEP7a5eUUTOX+O3C2RQfLzpw31Ro7pNo=',
            'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        session = requests.session()
        response = session.post("https://street-beat.ru/api/catalog/full", headers=headers, json=json_data)
        list = response.json()["catalog"]["listing"]["items"]
        with open("sneakers.json", "w", encoding="utf-8") as file:
            json.dump(list, file, indent=4, ensure_ascii=False)
        return len(list)
    except Exception:
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ru,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=UTF-8',
            'Cookie': 'rerf=AAAAAGO//255BLo7A026Ag==; ipp_uid=1673527149944/2KRGccKS3AuY3nhA/Y2ffoRNO0LRnWDko3z2uZQ==; __zzatinv-w-strbeat=MDA0dBA=Fz2+aQ==; BITRIX_SM_SALE_UID=1437421434; _gid=GA1.2.1903144150.1673527147; _ym_uid=167352714818532907; _ym_d=1673527148; tmr_lvid=2b7fffca76e5360c86b820d7007a4020; tmr_lvidTS=1673527148020; adrcid=APZ0ZEJ53DFitHLX35fOcQw; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; user_city=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; adspire_uid=AS.481304539.1673527149; atm_closer=%7B%22id%22%3A12690%2C%22mid%22%3A18509%2C%22aid%22%3A%22AS.481304539.1673527149%22%2C%22cookie_time%22%3A1673527149176%2C%22priority%22%3A0%7D; BX_USER_ID=d60081026a445bb3e98dc82c3b40ad89; MgidSensorUtmSource=yandex; MgidSensorClidV=0; flomni_62f613edb13909b07c8e81ed={%22userHash%22:%2243ff27e5-b520-4d7e-b737-f18fddd1e680%22}; mainpagetype=man; user_usee=a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%223985606%22%3Bi%3A1%3Bs%3A7%3A%223864034%22%3B%7D; PHPSESSID=Y6Jo9nfKLnaB9syFz1HOfr6VCkV7VOtp; ipp_key=v1673612112928/v33947245ba5adc7a72e273/Iu6urgN0+qErQgYXQ0NBgg==; topMenu_active=%2Fman%2F; _dc_gtm_UA-57250236-1=1; _ym_isad=2; _ym_visorc=w; _ga=GA1.2.359725046.1673527147; MgidSensorNVis=61; MgidSensorHref=https://street-beat.ru/cat/man/obuv/sale/; cfidsinv-w-strbeat=e5+G4yyKJI/lqzQBU/p+JywZPDDyHM4Wt852oHZzz23rK11QgbGkG7Am3VA2erDPug3mnqPcdvM22UTRzE3HMnqTZ5dTefuS4LJivZLGygBwuHjAUm6nbzjTn3rhmS1HI+anXwIdTpIWFHBf8uE6zDTejmVycM03jx2mVwQ=; cfidsinv-w-strbeat=e5+G4yyKJI/lqzQBU/p+JywZPDDyHM4Wt852oHZzz23rK11QgbGkG7Am3VA2erDPug3mnqPcdvM22UTRzE3HMnqTZ5dTefuS4LJivZLGygBwuHjAUm6nbzjTn3rhmS1HI+anXwIdTpIWFHBf8uE6zDTejmVycM03jx2mVwQ=; gsscinv-w-strbeat=eGK6OwygecZqQB5d3TMT1UTGusf5jq0O41m+5RcxID/2NQayHjSAbDdnq/YxkF9zuF630izQfcUoW9iqtC0ejnrRYLjbRMNFTrJjzJR0HtNQcVUBL+uh8vWX744l93ObouJoZUqsZJzbUKuLyhdwielzJluw/J9hnb0kpW45njcbkYfUtRasnKpfdb3qt9NuymlbnIiHmFquBmV9VkFQ8AOVYUWToaQItlbNl+bLxcPm2O2R2gw/eX3bnbwtv5TY39g=; tmr_detect=0%7C1673612148281; _ga_E3GN5VV3T0=GS1.1.1673612110.6.1.1673612155.0.0.0; mindboxDeviceUUID=401160c2-7b19-4196-b4be-f724465b04b1; directCrm-session=%7B%22deviceGuid%22%3A%22401160c2-7b19-4196-b4be-f724465b04b1%22%7D; fgsscinv-w-strbeat=CLDFf1bc5d4006aafe0a7b3fac5a40cdd5a2fdfc',
            'Origin': 'https://street-beat.ru',
            'Referer': 'https://street-beat.ru/cat/man/obuv/krossovki/adidas-originals/sale/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
            'X-GIB-FGSSCinv-w-strbeat': 'CLDFf1bc5d4006aafe0a7b3fac5a40cdd5a2fdfc',
            'X-GIB-GSSCinv-w-strbeat': 'eGK6OwygecZqQB5d3TMT1UTGusf5jq0O41m+5RcxID/2NQayHjSAbDdnq/YxkF9zuF630izQfcUoW9iqtC0ejnrRYLjbRMNFTrJjzJR0HtNQcVUBL+uh8vWX744l93ObouJoZUqsZJzbUKuLyhdwielzJluw/J9hnb0kpW45njcbkYfUtRasnKpfdb3qt9NuymlbnIiHmFquBmV9VkFQ8AOVYUWToaQItlbNl+bLxcPm2O2R2gw/eX3bnbwtv5TY39g=',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        session = requests.session()
        response = session.post("https://street-beat.ru/api/catalog/full", headers=headers, json=json_data)
        list = response.json()["catalog"]["listing"]["items"]
        with open("sneakers.json", "w", encoding="utf-8") as file:
            json.dump(list, file, indent=4, ensure_ascii=False)
        return len(list)


def next_street_beat():
    with open("sneakers.json", "r", encoding="utf-8") as file:
        sneakers = json.load(file)
    list = [sneakers[0]]
    sneakers.remove(sneakers[0])
    with open("sneakers.json", "w", encoding="utf-8") as file:
        json.dump(sneakers, file, indent=4, ensure_ascii=False)

    for item in list:
        url = "https://street-beat.ru" + item["url"]
        title = item["title"]
        price = item["price"]["special"]["price"]
        sale = int((item["price"]["recommended"]["price"] - price) / item["price"]["recommended"]["price"] * 100)
        yield url, title, "Цена: " + str(price) + "RUB", "Скидка🔥 " + str(sale) + "%"


