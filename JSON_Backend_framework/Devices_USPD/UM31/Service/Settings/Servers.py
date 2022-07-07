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

        # self.TCP = self._Generate_TCP()
        # self.SMTP = self._Generate_SMTP()
        # self.SNTP = self._Generate_SNTP()
        # self.MQTT = self._Generate_MQTT()

    # Здесь генерируем сам функционал :

    # Настройки TCP-серверов
    def _Generate_TCP(self):
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Servers.Server_TCP import ServerTCP
        TCP = ServerTCP(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return TCP

    # Настройки SMTP-серверов
    def _Generate_SMTP(self):
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Servers.Server_SMTP import ServerSMTP
        SMTP = ServerSMTP(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return SMTP

    # Настройки SТTP-серверов
    def _Generate_SNTP(self):
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Servers.Server_SNTP import ServerSNTP
        SNTP = ServerSNTP(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return SNTP

    # Настройки MQTT-серверов
    def _Generate_MQTT(self):
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Servers.Server_MQTT import ServerMQTT
        MQTT = ServerMQTT(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return MQTT
