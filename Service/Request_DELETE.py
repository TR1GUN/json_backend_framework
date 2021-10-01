from Service.TemplateRequest import TemplateRequest


# //////////////////////////////////////////////////////////////////////////////////////////
#                 Шаблон работы с методом DELETE
# //////////////////////////////////////////////////////////////////////////////////////////


class DELETE(TemplateRequest):
    """
    Класс Метода DELETE

    """
    # Переменная результата
    _result = {}

    def __init__(self, url: str, data=None, cookies=None, headers=None, ip_device=None):

        # обнуляем результат
        self._result = {}
        # Если изменен айпишник - то задаем его тоже
        if ip_device is not None:
            self.ip_port = str(ip_device)

        # Запускаем наш класс запроса
        response = self._Setup(url=url, data=data, cookies=cookies, headers=headers)

        # Переносим ответ в отдельное поле
        self._response = response

        # Теперь разбираем ответ
        self._Parse_result_code(response=response)
        self._Parse_JSON(response=response)

        if self._debug:
            print(self._result)

    def _Setup(self, url, data, cookies=None, headers=None):
        """
        :param url: Url запроса
        :return: Возвращает результат запроса
        """
        # Получаем наш адрес запроса
        url = self._url_collector(url=url)
        import requests
        # print(url)
        # Запускаем
        # Если дата есть
        if data is not None:
            # --->
            # ЕСли нет ни кук ни хедлесов
            if (cookies is None) and (headers is None):
                response = requests.delete(url, data=data)
            # Если есть куки
            elif cookies is not None:
                response = requests.delete(url, data=data, cookies=cookies)
            # Если есть хедлерс
            elif headers is not None:
                response = requests.delete(url, data=data, headers=headers)
            # Если есть и то и то
            elif (cookies is not None) and (headers is not None):
                response = requests.delete(url, data=data, headers=headers, cookies=cookies)
            # Иначе - отправляет просто
            else:
                response = requests.delete(url, data=data)
        # если даты нет
        else:
            # response = requests.delete(url)

            # ЕСли нет ни кук ни хедлесов
            if (cookies is None) and (headers is None):
                response = requests.delete(url)
            # Если есть куки
            elif cookies is not None:
                response = requests.delete(url, cookies=cookies)
            # Если есть хедлерс
            elif headers is not None:
                response = requests.delete(url, headers=headers)
            # Если есть и то и то
            elif (cookies is not None) and (headers is not None):
                response = requests.delete(url, headers=headers, cookies=cookies)
            # Иначе - отправляет просто
            else:
                response = requests.delete(url)

        # print(response)
        # Возвращаем данные
        return response

    def _Parse_result_code(self, response):
        """
        Парсим Результат запроса

        :param response: Результат опроса - тип данных - HTTPResponse
        :return:
        """

        self._result["code"] = response.status_code

    def _Parse_JSON(self, response):
        """
        Здесь Вытаскиваем JSON
        :param response: Результат опроса - тип данных - HTTPResponse
        :return:
        """

        try:
            self._result["data"] = response.json()

        # ЕСЛИ у нас ошибка - пытаемся вытащить текстовый файл
        except Exception as e:
            self._result["info"] = e
            self._Parse_text(response)

    def _Parse_text(self, response):
        """
        Здесь пытаемся вытащить текст
        :param response: Результат опроса - тип данных - HTTPResponse
        :return:
        """

        try:
            self._result["data"] = response.text
        except Exception as e:
            self._result["info"] = str(e) + "\n Текстовых данных нет"
            self._Parse_bytte_array(response)

    def _Parse_bytte_array(self, response):
        """
        Здесь смотрим что что то у нас есть хоть что-то  в байтах
        :param response: Результат опроса - тип данных - HTTPResponse
        :return:
        """
        try:
            self._result["data"] = response.raw
        except Exception as e:
            self._result["info"] = str(e) + "\n Байтовых данных нет>"
            self._result["data"] = False
