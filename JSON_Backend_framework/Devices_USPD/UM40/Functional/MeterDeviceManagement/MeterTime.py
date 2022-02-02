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

    Meter = None

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

        # Обнуляем конструктор
        self._define_JSON()

    def _getting_settings(self):

        """ Проверяем значение реле"""

        data = self.Meter.get_Meter()

        if data is None:
            data = {}

        # Обнуляем конструктор
        self._define_JSON()

        return data

    def _define_JSON(self):
        """
        Здесь Сбрасываем настройки
        """
        # Сбрасываем настройки
        self.Meter = SettingsMeterTimeSync()

# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data = {"id":1 }
# -------------------------------------------------------------------------------------------------------------
