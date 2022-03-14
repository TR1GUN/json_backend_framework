# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки SNTP-серверов
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.Servers.Template_SNTP_server_settings import \
    TemplateServer_SNTP


# -------------------------------------------------------------------------------------------------------------


class ServerSNTP(TemplateServer_SNTP):
    """

    Настройки SNTP-серверов

    Сервера синхронизации времени
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
        Настройки SNTP-серверов

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
#
# -------------------------------------------------------------------------------------------------------------

# print('read...')
# request = ServerSNTP().read_settings()
# print(request)
# print('write...')
# request = ServerTCP().write_settings()
# print(request)
# print('rewrete...')
# request = ServerTCP().rewrite_settings()
# print(request)