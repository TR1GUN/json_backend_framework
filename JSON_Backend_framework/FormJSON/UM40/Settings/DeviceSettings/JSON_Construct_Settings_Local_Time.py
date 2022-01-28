# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                     Настройки локального времени(Часовой пояс)
# -------------------------------------------------------------------------------------------------------------

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
    def add_DST(self, DST):
        self._DST = bool(DST)

    def remove_DST(self):
        self._DST = None

    def get_DST(self):
        return self._DST


class SettingsTimeZone:
    """

    Собираем в общий JSON

    """

    _Settings = None
    # Общие настройки
    TimeZone = TZ()

    DST = DST()

    def __init__(self):
        self._Settings = {}

    def get_TimeZone(self):

        """
        Получаем собранный JSON
        """
        tz = self.TimeZone.get_TimeZone()

        if tz is not None:

            self._Settings["tz"]: tz

        dst = self.DST.get_DST()

        if dst is not None:
            self._Settings['dst'] = dst

        return self._Settings


