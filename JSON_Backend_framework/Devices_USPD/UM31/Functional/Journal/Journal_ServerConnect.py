# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Получение Журнала сетевых подключений
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Journal.Template_Journal_ServerConnect import TemplateJournalServerConnect

# -------------------------------------------------------------------------------------------------------------


class JournalServerConnect(TemplateJournalServerConnect):
    """
    Получение Журнала сетевых подключений

    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Журнал сетевых подключений

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
# 	"Jrnl":[
# 		{
# 			"id":1,
# 			"time":"2018-08-27T10:19:52+03:00",
# 			"server":"192.168.202.95:80",
# 			"client":"218.18.6.32:54221",
# 			"iface":				2
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------