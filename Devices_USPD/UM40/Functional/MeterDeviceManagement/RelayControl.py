# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Управление реле
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from Service.Template_Devices_Functions.MeterManagement.Template_RelayControl import TemplateRelayControl


# -------------------------------------------------------------------------------------------------------------


class RelayControl(TemplateRelayControl):
    """
     Управление реле

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

    def Set_Relay(self, MeterIdx: int, RelayId: int, RelayState: int):
        """
        Установка положения реле на счетчике по его MeterIdx

        """

        data = {
                "id": int(MeterIdx),
                "relayId": int(RelayId),
                "relayState": int(RelayState),
                }

        result = self._Set_relay(data=data)

        return result

# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data = { "id": 1, "relayId": 1, "relayState": 1 }
# -------------------------------------------------------------------------------------------------------------
