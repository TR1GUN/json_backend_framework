# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Состояние линий питания интерфейсов УСПД
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.State.Template_State_DOut import TemplateStateDOut

# -------------------------------------------------------------------------------------------------------------


class StateDOut(TemplateStateDOut):
    """

    Состояние линий питания интерфейсов УСПД

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

    def read_State(self):
        """
        Чтение текущего времени на УСПД
        """

        return self._read_settings()

# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON - Здесь только чтение
# -------------------------------------------------------------------------------------------------------------
# data = {'State': [
#                   {'addr': '/dev/ttyUSB3', 'state': 'toggle'},
#                   {'addr': '/dev/ttyUSB2', 'state': 'toggle'},
#                   {'addr': '/dev/ttyUSB1', 'state': 'toggle'},
#                   {'addr': '/dev/ttyUSB0', 'state': 'toggle'}
#                   ]
#         }
# -------------------------------------------------------------------------------------------------------------
