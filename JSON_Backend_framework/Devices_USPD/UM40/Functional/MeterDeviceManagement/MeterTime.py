# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Установка времени на Счетчике
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.MeterManagement.Template_MeterTime import TemplateTimeMeterSetting


# -------------------------------------------------------------------------------------------------------------


class TimeMeterSetting(TemplateTimeMeterSetting):
    """
    Шаблон Установки времени на счетчике

    """
    # URL
    # from Devices_USPD.settings import url_path
    # _path_url = url_path.get("Settings_SIM")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Шаблон Установки времени на счетчике

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

    def Sync_time_to_meter(self, MeterIdx: int):
        """
        Синхронизация времени на счетчике по его MeterIdx

        """

        data = {"id": int(MeterIdx)}

        result = self._request_set_id(data=data)

        return result

# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data = {"id":1 }
# -------------------------------------------------------------------------------------------------------------
