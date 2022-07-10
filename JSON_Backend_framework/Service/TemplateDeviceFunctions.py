# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Шаблон работы с Функционалом УСПД - Можно вырезать
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Functional import TemplateFunctional
from JSON_Backend_framework.Service.TemplateDecorator import print_log_use_GET_data


# -------------------------------------------------------------------------------------------------------------
#                                         ПОЛЕ Settings
# -------------------------------------------------------------------------------------------------------------
class TemplateDeviceFunctions_Settings_WithOutDataTag(TemplateFunctional):
    """

    ШАБЛОН для поля - Настройки - здесь без поля Settings

    """
    # URL

    _path_url = ''

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Имя поля настроек
    _Settings_name = None

    # Настройки по умолчанию
    def Read_Settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET()

        return response

    def Write_Settings(self, data=None):
        """
        Добавляем на запись данные  - POST

        :param data:
        :return:
        """

        if data is None:
            data = self._getting_settings()

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def Rewrite_Settings(self, data=None):
        """
        Перезаписываем данные - PUT
        :param data:
        :return:
        """
        if data is None:
            data = self._getting_settings()

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_PUT(JSON=data)

        return response

    def Delete_Settings(self, data=None):
        """
        Удаляем данные - DELETE
        :param data:
        :return:
        """
        # Запаковываем
        if data is not None:
            data = self._coding(data=data)

            # делаем запрос - получаем ответ
            response = self._request_DELETE(JSON=data)
        else:
            # делаем запрос - получаем ответ
            response = self._request_DELETE()

        return response

    # Здесь расположим сервисные функции
    # Первое - Получаем настройки что уже есть

    def _getting_settings(self):

        """
        В Классе шаблоне метод получения настроек отвечает за вставку GET запроса

        """
        data = self._request_setting()
        return data

    # Запрос настроек
    def _request_setting(self):
        """
        Здесь запрашиваем нужные нам настройки

        """
        data = {}
        try:
            # делаем запрос - получаем ответ
            response = self.Read_Settings()
            # Теперь вытаскиваем нужное
            if response.get('code') == int(200):
                answer_setting = response.get('data')
                # Теперь заполянем наши переменные
                if answer_setting is not None:
                    data = answer_setting
        except Exception as e:

            print("При считывании параметров возникла ошибка - " + str(e))

        return data


class TemplateDeviceFunctions_Settings(TemplateFunctional):
    """

    ШАБЛОН для поля - Настройки - здесь с тегом для поля Settings

    """
    # URL

    _path_url = ''

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Имя поля настроек
    _Settings_name = ''

    # Настройки по умолчанию

    def Read_Settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET()

        return response

    def Write_Settings(self, data=None):
        """
        Добавляем на запись данные  - POST

        :param data:
        :return:
        """

        if data is None:
            data_settings = self._getting_settings()
            data = {self._Settings_name: data_settings}

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def Rewrite_Settings(self, data=None):
        """
        Перезаписываем данные - PUT
        :param data:
        :return:
        """
        if data is None:
            data_settings = self._getting_settings()
            data = {self._Settings_name: data_settings}

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_PUT(JSON=data)

        return response

    def Delete_Settings(self, data=None):
        """
        Удаляем данные - DELETE
        :param data:
        :return:
        """
        # Запаковываем
        if data is not None:
            data = self._coding(data=data)

            # делаем запрос - получаем ответ
            response = self._request_DELETE(JSON=data)
        else:
            # делаем запрос - получаем ответ
            response = self._request_DELETE()

        return response

    # Здесь расположим сервисные функции
    # Первое - Получаем настройки что уже есть

    def _getting_settings(self):

        """
        В Классе шаблоне метод получения настроек отвечает за вставку GET запроса
        """
        data = self._request_setting()
        return data

    # Запрос настроек
    @print_log_use_GET_data
    def _request_setting(self):
        """
        Здесь запрашиваем нужные нам настройки

        """
        data = []
        try:
            # делаем запрос - получаем ответ
            response = self.Read_Settings()
            # Теперь вытаскиваем нужное
            if response.get('code') == int(200):
                answer_setting = response.get('data')
                # Теперь заполянем наши переменные
                if answer_setting is not None:
                    Settings = answer_setting.get(self._Settings_name)
                    if Settings is not None:
                        data = Settings
        except Exception as e:

            print("При считывании параметров возникла ошибка - " + str(e))

        return data


# -------------------------------------------------------------------------------------------------------------
#                                         ПОЛЕ MeterData
# -------------------------------------------------------------------------------------------------------------

class TemplateDeviceFunctions_MeterData(TemplateFunctional):
    """
    Шаблон Опроса приборов учета

    """
    # URL

    _path_url = ''

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Доступные типы данных
    _measures = []

    def _Read(self, data):
        """
        Функция для прямой отправки JSON

        :param data: JSON
        :return:
        """
        # Запаковываем бэк
        data = self._coding(data=data)
        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response


# -------------------------------------------------------------------------------------------------------------
#                                         ПОЛЕ MeterManagement
# -------------------------------------------------------------------------------------------------------------
class TemplateDeviceFunctions_MeterManagement(TemplateFunctional):
    """
    Шаблон Управления счетчиком

    """
    # URL

    _path_url = ''

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url


# -------------------------------------------------------------------------------------------------------------
#                                         ПОЛЕ Actions
# -------------------------------------------------------------------------------------------------------------
# Поскольку здесь много бывает Методов - сделаем несколько шаблонов
# Задаем JSON
class TemplateDeviceFunctions_Actions_Set(TemplateFunctional):
    """

    Шаблон для действий - Задает значение

    """
    # URL

    _path_url = ''

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url

    def Set(self, data=None):
        """
        Задать данные - POST

        Формат JSON

        :param data: JSON На запись , который игнорирует

        """
        # Если мы дали пустоту , то определяем значения что заданы
        if data is None:
            data = self._define_data_set()
        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def _define_data_set(self):
        """
        В этом методе определяем данные что будем отправлять
        """

        # Поскольку здесь нельзя задать никакие данные , вставляем данные что будем считывать
        data = {}

        return data


# Синхронизация
class TemplateDeviceFunctions_Actions_Sync(TemplateFunctional):
    """

    Шаблон для действий - Задает значение

    """
    # URL

    _path_url = ''

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url

    def Sync(self):
        """
        Синхронизуем данные - POST

        Формат JSON
        """

        # делаем запрос - получаем ответ
        response = self._request_POST()

        return response


# -------------------------------------------------------------------------------------------------------------
#                                         ПОЛЕ InfoState
# -------------------------------------------------------------------------------------------------------------
class TemplateDeviceFunctions_InfoState(TemplateFunctional):
    """
     Шаблон  - Чтение состояния

    """
    # URL
    _path_url = ''

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Переопределяем чтоб можно было достать
    path_url = _path_url

    # Настройки по умолчанию

    def _read_settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET()

        return response

    def Read(self):
        """
        Чтение текущего времени на УСПД
        """

        return self._read_settings()


# -------------------------------------------------------------------------------------------------------------
#                                         ПОЛЕ Journal
# -------------------------------------------------------------------------------------------------------------


class TemplateDeviceFunctions_Journal(TemplateFunctional):
    """
    Шаблон Журнала

    """
    # URL

    _path_url = ''

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url

    # Настройки по умолчанию

    def Read_Journal(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET()

        return response


# -------------------------------------------------------------------------------------------------------------
#                                         ПОЛЕ Upload
# -------------------------------------------------------------------------------------------------------------


class TemplateDeviceFunctions_Upload(TemplateFunctional):
    """
    Шаблон Загрузки значений
    """
    # URL

    _path_url = ''

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url

    # Настройки по умолчанию

    def Upload(self, File):
        """
        Загружаем данные - POST
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_POST(File)

        return response

    def _request_POST(self, File):
        """
        Использование Метода POST

        :param JSON:
        :return:
        """
        from JSON_Backend_framework.Service.Request_Upload import Upload

        # Делаем запрос - получаем ответ - возвращаем
        response = Upload(url=self._path_url,
                          file=File,
                          cookies=self._cookies,
                          headers=self._headers,
                          ip_device=self._ip_address)
        # Получаем :
        # --->
        response_dict = self._parser_request(response=response)
        # --->
        return response_dict
