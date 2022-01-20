# Здесь опишем класс Авторизации
from JSON_Backend_framework.Devices_USPD.Authorization import Authorization


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Авторизация
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


class Authorization_UM40(Authorization):
    # Шаблон JSON для авторизации
    _data_Authorization = {'login': "admin", 'password': "admin"}
    # URL
    from JSON_Backend_framework.Devices_USPD.settings import url_path
    _path_url = url_path.get("Authorization")
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Куки для авторизации
    _cookies_to_authorization = None
    # IP Адрес

    _ip_address = 'localhost'

    _result = None