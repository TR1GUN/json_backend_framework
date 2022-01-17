# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки локального времени(Часовой пояс)
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.DeviceSettings.Template_Local_time_settings import \
    TemplateLocalTimeZone


# -------------------------------------------------------------------------------------------------------------
class TZ:
    """
    Настройки часового пояса

    """
    _TZ = None

    def __init__(self):
        self._TZ = None

    # Добавляем часовой пояс
    def add_TimeZone(self, TimeZone):
        self._TZ = TimeZone

    def remove_TimeZone(self):
        self._TZ = None

    def get_TimeZone(self):
        return self._TZ


class DST:
    """
    Настройки перевода часов

    """
    _DST = None

    def __init__(self):
        self._DST = None

    # Добавляем часовой пояс
    def add_TDST(self, DST):
        self._DST = bool(DST)

    def remove_DST(self):
        self._DST = None

    def get_DST(self):
        return self._DST


class TimeZone(TemplateLocalTimeZone):
    """
    Настройки локального времени(Часовой пояс)

    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    TimeZone = TZ()

    DST = DST()

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

    def _getting_settings(self):

        """
        Определяем данные что отдаем

        """
        tz = self.TimeZone.get_TimeZone()

        if tz is None:

            data = self._request_setting()

        else:
            data = {"tz": tz}

        dst = self.DST.get_DST()

        if dst is not None:
            data['dst'] = dst

        return data

# -------------------------------------------------------------------------------------------------------------
#                                           ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
#
# -------------------------------------------------------------------------------------------------------------
