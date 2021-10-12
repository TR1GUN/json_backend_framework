# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                               Мастер класс  от которого наследуемся
#                            Здесь будут задействованы основные запросы
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


class TemplateFunctional:
    """
    Мастер класс  от которого наследуемся
    Здесь будут задействованы основные запросы

    """
    # куки
    _cookies = None

    # Сам айпишник железки
    from Service.config import machine_ip
    _ip_address = str(machine_ip)

    # Путь url
    _path_url = ''

    # Клиент - Нужен для Хедерса
    _user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    # Страница с которой зашли - иногда нужно
    _Referer = 'http://192.168.0.1/login'

    # хедерс - Иногда нужен
    _headers = {
        'User-Agent': _user_agent,
        'Referer': 'http://192.168.0.1/login',
        'Host': '192.168.0.1',
        # 'Connection': keep-alive
        'Accept': '*/*',
        'Content-type': 'application/json',
        'Origin': 'http://192.168.0.1',
        # 'Cookie': 'sessionid=16349148992619061200'
    }

    # КОД Операции
    result_code = None
    data = None

    def _parser_request(self, response):
        """
        Считываем нужные данные
        :param response:
        :return: Возвращаем response_dict
        """
        # Код операции
        self.result_code = response.GET_result_code()
        # Текстовые данные , если есть
        self.data = response.GET_data()
        # куки
        cookies = response.get_cookies()
        # headers
        headers = response.get_headers()
        # Общий словарь данных
        response_dict = response.Result()

        return response_dict

    def _request_POST(self, JSON: str):
        """
        Использование Метода POST

        :param JSON:
        :return:
        """
        from Service.Request_POST import POST

        # Первое - удаляем все пробелы из строки JSON
        JSON = JSON.replace(" ", '')
        # Делаем запрос - получаем ответ - возвращаем
        response = POST(url=self._path_url,
                        data=JSON,
                        cookies=self._cookies,
                        headers=self._headers,
                        ip_device=self._ip_address)
        # Получаем :
        # --->
        response_dict = self._parser_request(response=response)
        # --->
        return response_dict

    def _request_GET(self, JSON: str = ''):
        """
        Использование Метода GET

        :param JSON:
        :return:
        """
        from Service.Request_GET import GET

        # Первое - удаляем все пробелы из строки JSON
        JSON = JSON.replace(" ", '')
        # Делаем запрос - получаем ответ - возвращаем
        response = GET(url=self._path_url,
                       cookies=self._cookies,
                       headers=self._headers,
                       ip_device=self._ip_address)
        # Получаем :
        # --->
        response_dict = self._parser_request(response=response)
        # --->
        return response_dict

    def _request_PUT(self, JSON: str):
        """
        Использование Метода PUT

        :param JSON:
        :return:
        """
        from Service.Request_PUT import PUT

        # Первое - удаляем все пробелы из строки JSON
        JSON = JSON.replace(" ", '')
        # Делаем запрос - получаем ответ - возвращаем

        response = PUT(url=self._path_url, data=JSON, cookies=self._cookies, headers=self._headers,
                       ip_device=self._ip_address)
        # Получаем :
        # --->
        response_dict = self._parser_request(response=response)
        # --->
        return response_dict

    def _request_DELETE(self, JSON: str = ''):
        """
        Использование Метода DELETE

        :param JSON:
        :return:
        """
        from Service.Request_DELETE import DELETE

        # Первое - удаляем все пробелы из строки JSON
        JSON = JSON.replace(" ", '')
        # Делаем запрос - получаем ответ - возвращаем
        response = DELETE(url=self._path_url, data=JSON, cookies=self._cookies, headers=self._headers,
                          ip_device=self._ip_address)
        # Получаем :
        # --->
        response_dict = self._parser_request(response=response)
        # --->
        return response_dict

    @staticmethod
    def _code_to_JSON(data):
        """
        Кодируем в JSON
        """
        from json import dumps

        return dumps(data)

    @staticmethod
    def _decode_from_JSON(data):
        """
        Кодируем в JSON
        """
        from json import loads

        return loads(data)

    def _coding(self, data):
        """
        Метод нужный для принудительного запаковывания в строку
        :param data:
        :return:
        """
        # Еcли это у нас словарь - кодируем в JSON
        if type(data) is dict:

            data = self._code_to_JSON(data=data)
        # Иначе - принудительно запаковываем в строку
        else:
            data = str(data)

        return data