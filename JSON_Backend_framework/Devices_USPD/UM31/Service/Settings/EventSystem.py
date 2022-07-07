# -------------------------------------------------------------------------------------------------------------
#                                     Поле Settings.EventSystem
# -------------------------------------------------------------------------------------------------------------

class SettingsEventSystem:
    _cookies = None
    _headers = None
    _ip_address = None

    # Настройки расписаний
    Scheduler = None
    # Настройки событий изменения состояния дискретных входов
    DIn = None
    # Настройки регулярного опроса приборов учета
    MeterPoller = None
    # Настройки регулярной отправки почтовых сообщений
    SMTP = None
    # Настройки регулярной синхронизации времени
    SNTP = None
    # Настройки регулярной отправки sms сообщений
    SMS = None
    # Настройки регулярной публикации mqtt сообщений
    MQTT = None

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
        # Настройки расписаний
        self.Scheduler = self._Events_Scheduler()
        # Настройки событий изменения состояния дискретных входов
        self.DIn = self._Events_DIn()
        # Настройки регулярного опроса приборов учета
        self.MeterPoller = self._Actions_MeterPoller()
        # Настройки регулярной отправки почтовых сообщений
        self.SMTP = self._Actions_SMTP()
        # Настройки регулярной синхронизации времени
        self.SNTP = self._Actions_SNTP()
        # Настройки регулярной отправки sms сообщений
        self.SMS = self._Actions_SMS()
        # Настройки регулярной публикации mqtt сообщений
        self.MQTT = self._Actions_MQTT()

    # Настройки расписаний
    def _Events_Scheduler(self):
        """
        Настройки расписаний
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.EventSystem.Events_Scheduler import Scheduler

        Events_Schedule = Scheduler(
                cookies=self._cookies,
                headers=self._headers,
                ip_address=self._ip_address
            )
        return Events_Schedule

    # Настройки событий изменения состояния дискретных входов
    def _Events_DIn(self):
        """
        Настройки событий изменения состояния дискретных входов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.EventSystem.Events_DIn import EventsDIn

        DIn = EventsDIn(
                cookies=self._cookies,
                headers=self._headers,
                ip_address=self._ip_address
            )
        return DIn

    # Настройки регулярного опроса приборов учета
    def _Actions_MeterPoller(self):
        """
        Настройки регулярного опроса приборов учета
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.EventSystem.Actions_MeterPoller import MeterPoller

        Poller = MeterPoller(
                cookies=self._cookies,
                headers=self._headers,
                ip_address=self._ip_address
            )
        return Poller

    # Настройки регулярной отправки почтовых сообщений
    def _Actions_SMTP(self):
        """
        Настройки регулярной отправки почтовых сообщений
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.EventSystem.Actions_SMTP import ActionsSMTP

        SMTP = ActionsSMTP(
                cookies=self._cookies,
                headers=self._headers,
                ip_address=self._ip_address
            )
        return SMTP

    # Настройки регулярной синхронизации времени
    def _Actions_SNTP(self):
        """
        Настройки регулярной синхронизации времени
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.EventSystem.Actions_SNTP import ActionsSNTP

        SNTP = ActionsSNTP(
                cookies=self._cookies,
                headers=self._headers,
                ip_address=self._ip_address
            )
        return SNTP

    # Настройки регулярной отправки sms сообщений
    def _Actions_SMS(self):
        """
        Настройки регулярной отправки sms сообщений
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.EventSystem.Actions_SMS import ActionsSMS

        SMS = ActionsSMS(
                cookies=self._cookies,
                headers=self._headers,
                ip_address=self._ip_address
            )
        return SMS

    # Настройки регулярной публикации mqtt сообщений
    def _Actions_MQTT(self):
        """
        Настройки регулярной публикации mqtt сообщений
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.EventSystem.Actions_MQTT import ActionsMQTT

        MQTT = ActionsMQTT(
                cookies=self._cookies,
                headers=self._headers,
                ip_address=self._ip_address
            )
        return MQTT