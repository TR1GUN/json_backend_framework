# Здесь расположим какие нить конфиги

# ЕСли их не будет - Удвалить


# Хедерс - У каждого протокола он свой
# =================================================================
#                   Версии Протокола
# =================================================================
# Хедер который определяет что у нас версия протокола УМ 40 СМАРТ
headers_protocol_UM40 = {
    "X-Protocol-USPD": 40,
    "X-Protocol-Version": 0.1,
}
# Хедер который определяет что у нас версия протокола УМ 31 СМАРТ
headers_protocol_UM31 = {
    "X-Protocol-USPD": 31,
    "X-Protocol-Version": 1.0,
}
# =================================================================
# Словарь с типом протокола - Хедерс
Type_Protocol_Headers_dict = {
    "UM40": headers_protocol_UM40,
    "UM31": headers_protocol_UM31,
}
# =================================================================
# Клиент - Нужен для Хедерса

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

# САМ хедерс
headers = {
        'User-Agent': user_agent,
        'Referer': 'http://192.168.0.1/login',
        'Host': '192.168.0.1',
        # 'Connection': keep-alive
        'Accept': '*/*',
        'Content-type': 'application/json',
        'Origin': 'http://192.168.0.1',
        # 'Cookie': 'sessionid=16349148992619061200'
    }
