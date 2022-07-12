# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Получение Журнала PPP подключений - Подключение сервера
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Journal.Template_Journal_PPP_ServerConnect import TemplateJournalPPPServerConnect

# -------------------------------------------------------------------------------------------------------------


class JournalPPPServerConnect(TemplateJournalPPPServerConnect):
    """
    Получение Журнала PPP подключений - Подключение сервера

    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Журнал PPP подключений - Подключение сервера

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
# 			"time":"2018-08-28T10:13:42+03:00",
# 			"res":				5
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------