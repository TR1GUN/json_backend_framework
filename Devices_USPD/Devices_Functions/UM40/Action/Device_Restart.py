# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         # Перезагрузка устройства
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from Service.Template_Functional import TemplateFunctional


class DeviceRestart(TemplateFunctional):
    """
    Перезагрузка устройства

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Device_Restart")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Настройки локального времени

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

    def Restart(self):
        """
        Берем и перезагружаем устройство
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET(JSON='')

        return response



# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


