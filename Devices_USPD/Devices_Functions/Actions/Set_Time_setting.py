# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Установка времени
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from Service.Template_Functional import TemplateFunctional


class SetTimeSetting(TemplateFunctional):
    """
    Установка времени

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Set_Time_setting")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Установка времени

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

        # print(self.headers)
        # print(self.cookies)

    # def read_settings(self):
    #     """
    #     Читаем данные - GET
    #     :return:
    #     """
    #     # делаем запрос - получаем ответ
    #     response = self._request_GET(JSON='')
    #
    #     return response

    def write_settings(self, data):
        """
        Добавляем на запись данные  - POST

        :param data:
        :return:
        """

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def setup_JSON(self, data):
        """
        Перезаписываем данные - PUT

        Формат JSON
        {"time": "2007-10-15T01:33:25+10:00"}

        :param data: JSON На запись , который игнорирует
        :return:
        """
        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_PUT(JSON=data)

        return response

    # def delete_settings(self, data=None):
    #     """
    #     Удаляем данные - DELETE
    #     :param data:
    #     :return:
    #     """
    #     # Запаковываем
    #     if data is not None:
    #         data = self._coding(data=data)
    #
    #         # делаем запрос - получаем ответ
    #         response = self._request_DELETE(JSON=data)
    #     else:
    #         # делаем запрос - получаем ответ
    #         response = self._request_DELETE()
    #
    #     return response

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# lol = SetTimeSetting().rewrite_settings(data={"time": "2007-10-15T01:33:25+10:00"})
# print(lol)

lol = SetTimeSetting().read_settings()
print(lol)
