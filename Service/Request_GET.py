from Service.TemplateRequest import TemplateRequest
# //////////////////////////////////////////////////////////////////////////////////////////
#                 Шаблон работы с методом GET
# //////////////////////////////////////////////////////////////////////////////////////////


class GET(TemplateRequest):
    """
    Класс Метода ГЕТ

    """
    # Переменная результата
    _result = {}

    def __init__(self, url: str):

        self._result = {}
        # Запускаем наш класс запроса
        response = self._Setup(url=url)

        # Теперь разбираем ответ
        self._Parse_result_code(response=response)
        self._Parse_JSON(response=response)

    def _Setup(self, url):
        """
        :param url: Url запроса
        :return: Возвращает результат запроса
        """
        # Получаем наш адрес запроса
        url = self.http + self.machine_ip + str(url)
        import requests
        # print(url)
        # Запускаем
        response = requests.get(url)

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
