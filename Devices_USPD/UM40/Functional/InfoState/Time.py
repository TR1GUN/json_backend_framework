# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Получение Текущего времени УСПД
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from Service.Template_Devices_Functions.State.Template_State_Time import TemplateStateTime

# -------------------------------------------------------------------------------------------------------------


class StateTime(TemplateStateTime):
    """
    Получение Текущего времени УСПД

    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Текущие время УСПД

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    def Time_USPD_Read(self):
        """
        Чтение текущего времени на УСПД
        """

        return self._read_settings()

# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON - Здесь только чтение
# -------------------------------------------------------------------------------------------------------------
# data = {'time': '2022-01-10T21:00:07+03:00', 'sync': False, 'state': True}
# -------------------------------------------------------------------------------------------------------------
