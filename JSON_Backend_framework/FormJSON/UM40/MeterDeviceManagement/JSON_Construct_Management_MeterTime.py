# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                           Установка времени на Счетчике
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------

class SettingsMeterTimeSync:
    _Setting_MeterTimeSync = None

    def __init__(self):
        self._Setting_MeterTimeSync = None

    def set_Meter(self, MeterIdx: int):
        """
        Установка положения реле на счетчике по его MeterIdx

        """

        data = {"id": int(MeterIdx)}

        self._Setting_MeterTimeSync = data

    def remove_Meter(self):
        """
        Удаление записанного положения Реле
        """
        self._Setting_MeterTimeSync = None

    def get_Meter(self):
        """ Получаем положение что задали """

        return self._Setting_MeterTimeSync

