# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Получение Журнал изменения состояния дискретных входов
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Journal.Template_Journal_DIn_Powerline import TemplateJournalDInPowerLine

# -------------------------------------------------------------------------------------------------------------


class JournalDInPowerLine(TemplateJournalDInPowerLine):
    """
    Получение Журнал изменения состояния дискретных входов

    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Журнал изменения состояния дискретных входов

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
# 			"time":"2018-08-29T07:09:04+03:00",
# 			"sens":0,
# 			"state":				1
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------