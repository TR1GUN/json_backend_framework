# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                 Состояние сетевых подключений
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.State.Template_State_Network import TemplateStateNetwork

# -------------------------------------------------------------------------------------------------------------


class StateNetwork(TemplateStateNetwork):
    """

    Состояние сетевых подключений

    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Состояние сетевых подключений

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON - Здесь только чтение
# -------------------------------------------------------------------------------------------------------------
# {
# 	"State":[
# 		{
# 			"name":"Ethernet",
# 			"ipaddr":"192.168.202.95",
# 			"netmask":"255.255.248.0",
# 			"gateway":"192.168.200.1",
# 			"hostname":"umrtump",
# 			"link":true
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------