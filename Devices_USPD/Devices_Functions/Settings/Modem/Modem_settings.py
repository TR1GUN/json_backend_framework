# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                      Шаблон Настройки модема
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# ЗДЕСЬ ОЧЕНЬ ВААЖНО - тут не используется поле Settings

from Service.Template_Functional import TemplateFunctional


class TemplateModem(TemplateFunctional):
    """
    Настройки модема

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Settings_Modem")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Имя поля настроек
    _Settings_name = None

    # Настройки по умолчанию

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

    def rewrite_settings(self, data=None):
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
            response = self.read_settings()
            # Теперь вытаскиваем нужное
            if response.get('code') == int(200):
                answer_setting = response.get('data')
                # Теперь заполянем наши переменные
                if answer_setting is not None:
                    data = answer_setting
        except Exception as e:

            print("При считывании параметров возникла ошибка - " + str(e))

        return data

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------