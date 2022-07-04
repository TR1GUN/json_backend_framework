# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки локального времени(Часовой пояс)
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.DeviceSettings.Template_Local_time_settings import \
    TemplateLocalTimeZone
from JSON_Backend_framework.FormJSON.UM40.Settings.DeviceSettings.JSON_Construct_Settings_Local_Time import SettingsTimeZone
# -------------------------------------------------------------------------------------------------------------


class TimeZone(TemplateLocalTimeZone):
    """
    Настройки локального времени(Часовой пояс)
    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    Settings = None

    # Настройки по умолчанию

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Настройки локального времени(Часовой пояс)

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address
        # Обнуляем
        self._define_JSON()

    def _define_JSON(self):
        """
        Здесь Сбрасываем настройки
        """
        # Сбрасываем настройки
        self.Settings = SettingsTimeZone()


    def _getting_settings(self):

        """
        Определяем данные что отдаем

        """
        data_Settings = self.Settings.get_TimeZone()
        tz = data_Settings.get("tz")
        dst = data_Settings.get("dst")
        # Обнуляем
        self._define_JSON()

        if tz is None:

            data = self._request_setting()

        else:
            data = {"tz": tz}

        if dst is not None:
            data['dst'] = dst

        return data

# -------------------------------------------------------------------------------------------------------------
#                                           ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data = {
# 	        "tz":3,
# 	        "dst":false
#         }
# -------------------------------------------------------------------------------------------------------------
