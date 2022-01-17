# -------------------------------------------------------------------------------------------------------------
#                                     Поле Settings.Modem
# -------------------------------------------------------------------------------------------------------------

class SettingsModem:
    _cookies = None
    _headers = None
    _ip_address = None

    # Настройки SIM-карт (Pin, APN)
    SIM = None
    # Настройки CSD(PPP-сервер)
    CSD = None
    # Настройки APN(точки доступа)
    APN = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address

        self.SIM = self._Generate_SIM_card()

    # Здесь генерируем сам функционал :

    # ГЕНЕРИРУЕМ Таблица приборов учета
    def _Generate_SIM_card(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.Modem.SIM_card_settings import SIM_card
        SIM_card = SIM_card(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return SIM_card
