# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Шаблон работы с Функционалом УСПД
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from Service.Template_Functional import TemplateFunctional


class TemplateDeviceFunctions(TemplateFunctional):
    """

    Шаблон работы с функционалом USPD

    """
    # URL
    _path_url = ''

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    Data_Settings = None

    # def __init__(self, cookies=None, headers=None, ip_address=None):
    #     """
    #
    #
    #     :param cookies:
    #     :param headers:
    #     """
    #     if cookies is not None:
    #         self._cookies = cookies
    #     if headers is not None:
    #         self._headers = headers
    #
    #     if ip_address is not None:
    #         self._ip_address = ip_address
    #
    #     self._data_settings = []
    #     self._data_ids = []
    # print(self.cookies)
    def _define_settings_ids(self):
        """

        Здесь обновляем Поля настроек

        :return:
        """

        self.Data_Settings = TemplateSettingsData()

    def read_settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET(JSON='')

        return response

    def write_settings(self, data=None):
        """
        Добавляем на запись данные  - POST

        :param data: Данные в Формате JSON - Если None - то используем добавленные данные
        :return:
        """
        if data is None:

            data_settings = self.Data_Settings.get_settings()
            data = {'settings': data_settings}

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def rewrite_settings(self, data):
        """
        Перезаписываем данные - PUT
        :param data: Данные в Формате JSON - Если None - то используем добавленные данные
        :return:
        """
        if data is None:
            data_settings = self.Data_Settings.get_settings()
            data = {'settings': data_settings}

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_PUT(JSON=data)

        return response

    def delete_settings(self, data=None):
        """
        Удаляем данные - DELETE
        :param data:
        :return:
        """

        if data is None:

            data_settings = self.Data_Settings.get_ids()

            if len(data_settings) > 0:
                data = {'settings': data_settings}
            else:
                data = None

        # Запаковываем
        if data is not None:
            data = self._coding(data=data)

            # делаем запрос - получаем ответ
            response = self._request_DELETE(JSON=data)
        else:
            # делаем запрос - получаем ответ
            response = self._request_DELETE()

        return response


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Шаблон работы с Функционалом УСПД
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

class TemplateSettingsData:
    """

    Класс Шаблон Для поля Settings

    """
    _data_settings = []
    _data_ids = []
    # def __init__(self):
    #
    #     self._data_settings = []

    def add_settings(self,*args, **kwargs):
        """
        Добавление настроек для записи

        :return:
        """
        settings = {}

        self._data_settings.append(settings)

    def remove_settings(self, idx: [int, list]):
        """
        Удаление добавленной записи settings для записи по ID
        :param idx: - list or int
        :return:
        """
        data_settings = []

        # Перебираем все настройки
        for settings in self._data_settings:
            # Если айдишник не совпадает то добавляем в список
            if settings.get('id') not in idx:
                data_settings.append(settings)

        self._data_settings = data_settings

    def get_settings(self):
        """
        Получаем добавленные settings

        :return:
        """

        return self._data_settings

    def add_ids(self, ids: int):
        """
        Добавляем Device_id для запроса данных или удаления

        :param ids:
        :return:
        """

        self._data_ids.append(ids)

    def remove_ids(self, ids: [int, list]):
        """
        Удаление добавленной записи ids для получения/удаления записей
        :param ids: - list or int
        :return:
        """
        data_ids = []

        # Перебираем все настройки
        for idx in self._data_ids:
            # Если айдишник не совпадает то добавляем в список
            if idx not in ids:
                data_ids.append(settings)

        self._data_ids = data_ids

    def get_ids(self):
        """
        Получаем добавленные settings

        :return:
        """

        return self._data_ids
