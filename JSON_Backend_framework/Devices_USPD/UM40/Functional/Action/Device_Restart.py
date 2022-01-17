# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         # Перезагрузка устройства
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Devices_Functions.Actions.Template_DeviceRestart import TemplateDeviceRestart


class DeviceRestart(TemplateDeviceRestart):
    """
    Перезагрузка устройства

    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Перезагрузка устройства

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

        # print(self.headers)
        # print(self.cookies)


# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON - Здесь только чтение
# -------------------------------------------------------------------------------------------------------------

