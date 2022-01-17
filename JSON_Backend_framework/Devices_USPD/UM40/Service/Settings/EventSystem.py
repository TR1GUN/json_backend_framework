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

    # Настройки регулярной публикации mqtt сообщений
    MQTT = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address

        self.Calendar = self._Generate_Calendar()
        self.Scheduler = self._Generate_Scheduler()
        self.Manager = self._Generate_Manager()
        self.TemplatesMeter = self._Generate_TemplatesMeter()
        self.TemplatesMeterData = self._Generate_TemplatesMeterData()
        self.Messages = self._Generate_Messages()
        self.Email = self._Generate_Email()
        self.MeterPoller = self._Generate_MeterPoller()
        self.SMTP = self._Generate_SMTP()
        self.SNTP = self._Generate_SNTP()
        self.MQTT = self._Generate_MQTT()

    # Здесь генерируем сам функционал :

    # ГЕНЕРИРУЕМ Таблица приборов учета
    def _Generate_Calendar(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Events_Calendar import Calendar

        Events_Calendar = Calendar(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_Calendar

    # ГЕНЕРИРУЕМ Настройки хранения архивных данных приборов учета
    def _Generate_Scheduler(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Events_Scheduler import Schedule

        Events_Schedule = Schedule(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_Schedule

    # ГЕНЕРИРУЕМ Таблица приборов учета
    def _Generate_Manager(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Events_Manager import EventManager

        Events_EventManager = EventManager(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_EventManager

    # ГЕНЕРИРУЕМ Настройки хранения архивных данных приборов учета
    def _Generate_TemplatesMeter(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Templates_Meter import TemplatesMeter

        Events_TemplatesMeter = TemplatesMeter(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_TemplatesMeter

    # ГЕНЕРИРУЕМ Таблица приборов учета
    def _Generate_TemplatesMeterData(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Templates_MeterData import TemplatesMeterData

        Events_TemplatesMeterData = TemplatesMeterData(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_TemplatesMeterData

    # ГЕНЕРИРУЕМ Настройки хранения архивных данных приборов учета
    def _Generate_Messages(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Templates_Messages import TemplatesMessages

        Events_TemplatesMessages = TemplatesMessages(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_TemplatesMessages

    # ГЕНЕРИРУЕМ Таблица приборов учета
    def _Generate_Email(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Templates_Email import TemplatesEmail

        Events_TemplatesEmail = TemplatesEmail(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_TemplatesEmail

    # ГЕНЕРИРУЕМ Настройки хранения архивных данных приборов учета
    def _Generate_MeterPoller(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Actions_MeterPoller import MeterPoller

        Events_MeterPoller = MeterPoller(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_MeterPoller

    # ГЕНЕРИРУЕМ Таблица приборов учета
    def _Generate_SMTP(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Actions_SMPT import ActionsSMTP

        Events_ActionsSMTP = ActionsSMTP(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_ActionsSMTP

    # ГЕНЕРИРУЕМ Настройки хранения архивных данных приборов учета
    def _Generate_SNTP(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Actions_SNTP import ActionsSNTP

        Events_ActionsSNTP = ActionsSNTP(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_ActionsSNTP

    # ГЕНЕРИРУЕМ Настройки хранения архивных данных приборов учета
    def _Generate_MQTT(self):
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Settings.EventSystem.Actions_MQTT import ActionsMQTT

        Events_ActionsMQTT = ActionsMQTT(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Events_ActionsMQTT