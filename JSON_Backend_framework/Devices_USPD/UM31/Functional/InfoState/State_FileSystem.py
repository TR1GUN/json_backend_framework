# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                        Состояние файловой системы
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.State.Template_State_FileSystem import TemplateStateFileSystem

# -------------------------------------------------------------------------------------------------------------


class StateFileSystem(TemplateStateFileSystem):
    """

    Состояние файловой системы

    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Состояние файловой системы

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
# 	"ssize":4096,
# 	"State":[
# 		{
# 			"num":0,
# 			"info":"0:fwupdate",
# 			"size":507,
# 			"free":507
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------
