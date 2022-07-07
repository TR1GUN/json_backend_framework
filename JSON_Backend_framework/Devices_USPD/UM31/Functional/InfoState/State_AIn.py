# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                  Состояние аналоговых входов УСПД
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.State.Template_State_AIn import TemplateStateAIn

# -------------------------------------------------------------------------------------------------------------


class StateAIn(TemplateStateAIn):
    """

    Состояние аналоговых входов УСПД

    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Состояние аналоговых входов УСПД

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
# 			"addr":0,
# 			"state":12
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------
