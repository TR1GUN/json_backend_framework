# -------------------------------------------------------------------------------------------------------------
#                                     Поле Settings.Modem
# -------------------------------------------------------------------------------------------------------------

class SettingsModem:
    _cookies = None
    _headers = None
    _ip_address = None

    # Настройки Модема (Pin)
    Modem = None
    # Настройки CSD(PPP-сервер)
    CSD = None
    # Настройки APN(точки доступа)
    APN = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address

        # Обновляем функционал
        # ---->
        self._define_functionality()

    def _define_functionality(self):
        """
        Получение функционала
        """
        # Настройки Модема (Pin)
        self.Modem = self._Modem_Settings()
        # Настройки CSD(PPP-сервер)
        self.CSD = self._Modem_CSD()
        # Настройки APN(точки доступа)
        self.APN = self._Modem_APN()

    # Здесь генерируем сам функционал :
    # Настройки Модема (Pin)
    def _Modem_Settings(self):
        """
        # Настройки Модема (Pin)
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Modem.Modem_SIM import ModemSIM
        SIM_card = ModemSIM(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return SIM_card

    # Настройки CSD(PPP-сервер)
    def _Modem_CSD(self):
        """
        Настройки CSD(PPP-сервер)
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Modem.Modem_CSD import ModemCSD
        CSD = ModemCSD(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return CSD

    # Настройки APN(точки доступа)
    def _Modem_APN(self):
        """
        Настройки APN(точки доступа)
        :return:
        """

        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Modem.Modem_APN import ModemAPN
        APN = ModemAPN(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return APN