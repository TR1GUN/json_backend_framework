# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         # Обновление ВПО
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.Template_Devices_Functions.Upload.Template_Upload_Firmware import \
    TemplateUpLoadFirmware


class UpLoadFirmware(TemplateUpLoadFirmware):
    """
    Обновление ВПО

    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Обновление ВПО

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
#                          ПРИМЕР JSON - Здесь спускаем файл
# -------------------------------------------------------------------------------------------------------------
