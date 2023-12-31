# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки SMTP-серверов
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.Servers.Template_SMTP_server_settings import \
    TemplateServer_SMTP


# -------------------------------------------------------------------------------------------------------------


class ServerSMTP(TemplateServer_SMTP):
    """

    Настройки SMTP-серверов
    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    # Settings = None

    # Настройки по умолчанию

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Настройки SMTP-серверов

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
#                                           ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# {
# 	"Settings":[
# 		{
# 			"email":"test@gmail.com",
# 			"server":"smtp.gmail.com",
# 			"userName":"test",
# 			"port":587,
# 			"id":1,
# 			"userPassword":"4c5cgc45hw"
# 		}
# 	]
# }
# -------------------------------------------------------------------------------------------------------------
