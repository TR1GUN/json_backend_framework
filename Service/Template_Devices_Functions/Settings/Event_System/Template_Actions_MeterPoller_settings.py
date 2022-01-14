# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                     ШАБЛОН Настройки регулярного опроса приборов учета
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from Service.Template_Functional import TemplateFunctional


class TemplateActionsMeterPoller(TemplateFunctional):
    """
    ШАБЛОН Настройки регулярного опроса приборов учета

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Actions_Meter_Poller")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Имя поля настроек
    _Settings_name = 'Settings'

    # Настройки по умолчанию

    def read_settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET()

        return response

    def write_settings(self, data=None):
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

    def rewrite_settings(self, data=None):
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

    def delete_settings(self, data=None):
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

        В Классе шаблоне метод получения настроек отвечает за встравку GET запроса


        """
        data = self._request_setting()
        return data

    # Запрос настроек
    def _request_setting(self):
        """
        Здесь запрашиваем нужные нам настройки

        """
        data = []
        try:
            # делаем запрос - получаем ответ
            response = self.read_settings()
            # Теперь вытаскиваем нужное
            if response.get('code') == int(200):
                answer_setting = response.get('data')
                # Теперь заполянем наши переменные
                if answer_setting is not None:
                    Settings = answer_setting[self._Settings_name]
                    if Settings is not None :
                        data = Settings
        except Exception as e:

            print("При считывании параметров возникла ошибка - " + str(e))

        return data

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------