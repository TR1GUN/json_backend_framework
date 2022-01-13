# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки регулярного опроса приборов учета
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from Service.Template_Devices_Functions.Settings.Event_System.Template_Actions_MeterPoller_settings import \
    TemplateActionsMeterPoller


# -------------------------------------------------------------------------------------------------------------


class MeterPoller(TemplateActionsMeterPoller):
    """
    Настройки регулярного опроса приборов учета

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
        Настройки регулярного опроса приборов учета

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