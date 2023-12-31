# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Получение Журнал системы событий
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Journal.Template_Journal_Action import TemplateJournalAction

# -------------------------------------------------------------------------------------------------------------


class JournalAction(TemplateJournalAction):
    """
    Получение Журнал системы событий

    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Журнал Журнал системы событий

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
# 			"action":{
# 				"id":1,
# 				"type":"Poller"
# 			},
# 			"event":{
# 				"id":1,
# 				"type":"Scheduler"
# 			},
# 			"time":1234567890
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------
