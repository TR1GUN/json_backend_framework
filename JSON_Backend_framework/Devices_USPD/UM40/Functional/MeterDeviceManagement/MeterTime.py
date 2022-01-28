# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Установка времени на Счетчике
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.MeterManagement.Template_MeterTime import \
    TemplateTimeMeterSetting
from JSON_Backend_framework.FormJSON.UM40.MeterDeviceManagement.JSON_Construct_Management_MeterTime import SettingsMeterTimeSync

# -------------------------------------------------------------------------------------------------------------


class TimeMeterSetting(TemplateTimeMeterSetting):
    """
    Шаблон Установки времени на счетчике

    """
    # URL

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    Meter = SettingsMeterTimeSync()

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Шаблон Установки времени на счетчике

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    def _getting_settings(self):

        """ Проверяем значение реле"""

        data = self.Meter.get_Meter()

        if data is None:
            data = {}
        return data

    def Sync(self, data=None):
        """
        Синхронизация времени на счетчике по его MeterIdx

        """
        if data is None:
            data = self._getting_settings()

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data = {"id":1 }
# -------------------------------------------------------------------------------------------------------------
