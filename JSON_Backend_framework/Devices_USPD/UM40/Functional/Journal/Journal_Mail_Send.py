# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Получение Журнала отправки почтовых сообщений
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Journal.Template_Journal_Mail_Send import TemplateJournalMailSend

# -------------------------------------------------------------------------------------------------------------


class JournalMailSend(TemplateJournalMailSend):
    """
    Получение Журнала отправки почтовых сообщений

    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Журнал отправки почтовых сообщений

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
# 			"id":205,
# 			"time":"2018-09-03T03:49:08+03:00",
# 			"idMsg":1549643952,
# 			"idSrv":1,
# 			"idTo":1,
# 			"res":				19
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------