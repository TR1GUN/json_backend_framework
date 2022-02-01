# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                       ШАБЛОН  Настройки Ethernet
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Здесь не будем ничего мудрить - так как в 31 и в 40 они по разному прописываются
# в 40 через поле settings
# в 31 через простой список
#
from JSON_Backend_framework.Service.Template_Functional import TemplateFunctional
from JSON_Backend_framework.Devices_USPD.settings import url_path


class TemplateInterface_Ethernet(TemplateFunctional):
    """
    Настройки Ethernet

    """
    from JSON_Backend_framework.Service.TemplateDecorator import print_log_use_GET_data

    # URL

    _path_url = url_path.get("Settings_Ethernet")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Переопределяем чтоб можно было достать
    path_url = _path_url
    # Имя поля настроек
    Ethernet_Settings = None

    _settings_to_send = {}

    # Настройки по умолчанию

    def Read_settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET()

        return response

    def Write_settings(self, data=None):
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

    def Rewrite_settings(self, data=None):
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

    def Delete_settings(self, data=None):
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
        data = {}
        try:
            # делаем запрос - получаем ответ
            response = self.Read_settings()
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