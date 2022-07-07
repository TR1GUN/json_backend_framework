# -------------------------------------------------------------------------------------------------------------
#                                     Поле Settings.Servers
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

        # ---->
        self._define_functionality()

    def _define_functionality(self):
        """
        Получение функционала
        """
        # Настройки TCP-серверов
        self.TCP = self._Servers_TCP()
        # Настройки SMTP-серверов
        self.SMTP = self._Servers_SMTP()
        # Настройки SNTP-серверов
        self.SNTP = self._Servers_SNTP()
        # Настройки MQTT-серверов
        self.MQTT = self._Servers_MQTT()

    # Здесь генерируем сам функционал :

    # Настройки TCP-серверов
    def _Servers_TCP(self):
        """
        Настройки TCP-серверов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Servers.Server_TCP import ServerTCP
        TCP = ServerTCP(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return TCP

    # Настройки SMTP-серверов
    def _Servers_SMTP(self):
        """
        Настройки SMTP-серверов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Servers.Server_SMTP import ServerSMTP
        SMTP = ServerSMTP(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return SMTP

    # Настройки SТTP-серверов
    def _Servers_SNTP(self):
        """
        Настройки SТTP-серверов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Servers.Server_SNTP import ServerSNTP
        SNTP = ServerSNTP(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return SNTP

    # Настройки MQTT-серверов
    def _Servers_MQTT(self):
        """
        Настройки MQTT-серверов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Servers.Server_MQTT import ServerMQTT
        MQTT = ServerMQTT(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return MQTT
