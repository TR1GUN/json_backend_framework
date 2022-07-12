# -------------------------------------------------------------------------------------------------------------
#                                     Поле Settings.EventSystem
# -------------------------------------------------------------------------------------------------------------

class SettingsEventSystem:
    _cookies = None
    _headers = None
    _ip_address = None

    # Настройки событий календаря
    Calendar = None
    # Настройки расписаний
    Scheduler = None
    # Настройки менеджера системы событий
    Manager = None
    # Настройки шаблонов приборов учета
    TemplatesMeter = None
    # Настройки шаблонов данных приборов учета
    TemplatesMeterData = None
    # Настройки шаблонов сообщений
    Messages = None
    # Шаблоны Email адресов
    Email = None
    # Настройки регулярного опроса приборов учета
    MeterPoller = None
    # Настройки регулярной отправки почтовых сообщений
    SMTP = None
    # Настройки регулярной синхронизации времени
    SNTP = None
    # Настройки регулярной отправки sms сообщений
    # SMS = None
    # Настройки регулярной публикации mqtt сообщений
    MQTT = None

    # # Настройки событий изменения состояния дискретных входов
    # DIn = None

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

        # Настройки событий календаря
        self.Calendar = self._Events_Calendar()
        # Настройки расписаний
        self.Scheduler = self._Events_Scheduler()
        # # Настройки событий изменения состояния дискретных входов
        # self.DIn = self._Events_DIn()
        # Настройки менеджера системы событий
        self.Manager = self._Events_Manager()
        # Настройки шаблонов приборов учета
        self.TemplatesMeter = self._Templates_Meter()
        # Настройки шаблонов данных приборов учета
        self.TemplatesMeterData = self._Templates_MeterData()
        # Настройки шаблонов сообщений
        self.Messages = self._Templates_Messages()
        # Шаблоны Email адресов
        self.Email = self._Templates_Email()
        # Настройки регулярного опроса приборов учета
        self.MeterPoller = self._Actions_MeterPoller()
        # Настройки регулярной отправки почтовых сообщений
        self.SMTP = self._Actions_SMTP()
        # Настройки регулярной синхронизации времени
        self.SNTP = self._Actions_SNTP()
        # # Настройки регулярной отправки sms сообщений
        # self.SMS = self._Actions_SMS()
        # Настройки регулярной публикации mqtt сообщений
        self.MQTT = self._Actions_MQTT()

    # Настройки расписаний
    def _Events_Scheduler(self):
        """
        Настройки расписаний
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Events_Scheduler import Scheduler

        Events_Schedule = Scheduler(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_Schedule

    # # Настройки событий изменения состояния дискретных входов
    # def _Events_DIn(self):
    #     """
    #     Настройки событий изменения состояния дискретных входов
    #     :return:
    #     """
    #     from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Events_DIn import EventsDIn
    #
    #     DIn = EventsDIn(
    #             cookies=self._cookies,
    #             headers=self._headers,
    #             ip_address=self._ip_address
    #         )
    #     return DIn

    # Настройки регулярного опроса приборов учета
    def _Actions_MeterPoller(self):
        """
        Настройки регулярного опроса приборов учета
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Actions_MeterPoller import \
            MeterPoller

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
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Actions_SMTP import ActionsSMTP

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
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Actions_SNTP import ActionsSNTP

        SNTP = ActionsSNTP(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return SNTP

    # # Настройки регулярной отправки sms сообщений
    # def _Actions_SMS(self):
    #     """
    #     Настройки регулярной отправки sms сообщений
    #     :return:
    #     """
    #     from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Actions_SMS import ActionsSMS
    #
    #     SMS = ActionsSMS(
    #             cookies=self._cookies,
    #             headers=self._headers,
    #             ip_address=self._ip_address
    #         )
    #     return SMS

    # Настройки регулярной публикации mqtt сообщений
    def _Actions_MQTT(self):
        """
        Настройки регулярной публикации mqtt сообщений
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Actions_MQTT import ActionsMQTT

        MQTT = ActionsMQTT(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return MQTT

    # Настройки событий календаря
    def _Events_Calendar(self):
        """
        Настройки событий календаря
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Events_Calendar import Calendar

        Events_Calendar = Calendar(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_Calendar

    # Настройки менеджера системы событий
    def _Events_Manager(self):
        """
        Настройки менеджера системы событий
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Events_Manager import EventManager

        Events_EventManager = EventManager(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_EventManager

    # Настройки шаблонов приборов учета
    def _Templates_Meter(self):
        """
        Настройки шаблонов приборов учета
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Templates_Meter import \
            TemplatesMeter

        Events_TemplatesMeter = TemplatesMeter(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_TemplatesMeter

    # Настройки шаблонов данных приборов учета
    def _Templates_MeterData(self):
        """
        Настройки шаблонов данных приборов учета
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Templates_MeterData import \
            TemplatesMeterData

        Events_TemplatesMeterData = TemplatesMeterData(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_TemplatesMeterData

    # Настройки шаблонов сообщений
    def _Templates_Messages(self):
        """
        Настройки шаблонов сообщений
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Templates_Messages import \
            TemplatesMessages

        Events_TemplatesMessages = TemplatesMessages(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_TemplatesMessages

    # Шаблоны Email адресов
    def _Templates_Email(self):
        """
        Шаблоны Email адресов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Templates_Email import \
            TemplatesEmail

        Events_TemplatesEmail = TemplatesEmail(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_TemplatesEmail
