# -------------------------------------------------------------------------------------------------------------
#                                     Поле Settings.Modem
# -------------------------------------------------------------------------------------------------------------

class SettingsServers:
    _cookies = None
    _headers = None
    _ip_address = None

    # Настройки TCP-серверов
    TCP = None
    # Настройки SMTP-серверов
    SMTP = None
    # Настройки SТTP-серверов
    SNTP = None
    # Настройки MQTT-серверов
    MQTT = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address

        self.SIM = self._Generate_SIM_card()

    # Здесь генерируем сам функционал :

    # ГЕНЕРИРУЕМ Таблица приборов учета
    def _Generate_SIM_card(self):
        from Devices_USPD.UM40.Functional.Settings.Modem.SIM_card_settings import SIM_card
        SIM_card = SIM_card(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return SIM_card
