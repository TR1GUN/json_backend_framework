# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                             УМ - 40 СМАРТ - Поле Upload
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.TemplateUSPD import Template_UM_XX_SMART_Upload


class UM_40_SMART_UpLoad(Template_UM_XX_SMART_Upload):
    """
    Саб класс который работает с разделом УСПД : Загрузка ВПО
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал
    # Загрузка файлов обновления ВПО
    Firmware = None
    # # Загрузка файлов обновления загрузчика
    # Loader = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address

        # ---->

        self._define_functionality()

    def _define_functionality(self):
        """

        Получение функционала

        """

        # Загрузка файлов обновления ВПО
        self.Firmware = self._Upload_Firmware()
        # # Загрузка файлов обновления загрузчика
        # self.Loader = self._Upload_Loader()

    # Загрузка файлов обновления ВПО
    def _Upload_Firmware(self):
        """
        Загрузка файлов обновления ВПО
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Upload.Upload_Firmware import  UpLoadFirmware
        Firmware = UpLoadFirmware(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Firmware

    # # Загрузка файлов обновления загрузчика
    # def _Upload_Loader(self):
    #     """
    #     Загрузка файлов обновления загрузчика
    #     """
    #     from JSON_Backend_framework.Devices_USPD.UM40.Functional.Upload.Upload_Loader import UpLoadLoader
    #
    #     Loader = UpLoadLoader(
    #         cookies=self._cookies,
    #         headers=self._headers,
    #         ip_address=self._ip_address
    #     )
    #     return Loader
