# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 40 СМАРТ - Поле Journal
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.TemplateUSPD import Template_UM_XX_SMART_Journal


class UM_40_SMART_Journal(Template_UM_XX_SMART_Journal):
    """
    Саб класс который работает с разделом УСПД :  : Журналы
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал

    # Журнал системы событий
    Action = None
    # Журнал изменения времени
    Time = None
    # Журнал сетевых подключений
    ServerConnect = None
    # Журнал PPP подключений - Клиент
    PPP_ClientConnect = None
    # Журнал PPP подключений - Сервер
    PPP_ServerConnect = None
    # Журнал входящих вызовов (CSD)
    Call = None
    # Журнал изменения состояния дискретных входов
    DIn_Sens = None
    # Журнал изменения состояния дискретных входов
    DIn_Powerline = None
    # Журнал изменения состояния дискретных входов
    DIn_Power = None
    # Журнал изменения состояния дискретных входов
    DIn_Charge = None
    # Журнал изменения состояния дискретных входов
    DIn_Open = None
    # 	Журнал авторизации
    Auth_JSON = None
    # 	Журнал перезагрузок
    Reset = None
    # 	Журнал хранилища почтовых сообщений
    Mail_Message = None
    # 	Журнал отправки почтовых сообщений
    Mail_Send = None
    # 	Журнал изменения версии ВПО изделия
    Update_Version = None
    # Журнал обновления ВПО загрузчика
    Update_Loader = None
    # 	Журнал фиксации ответов приборов учета
    Meter_Answer = None
    # 	Журнал хранилища исходящих SMS сообщений
    SMS_Message = None
    # 	Журнал отправки SMS
    SMS_Send = None
    # 	Журнал приема SMS
    SMS_Get = None
    # 	Журнал установки связи с MQTT-брокером
    MQTT_Connect = None
    # Журнал обмена сообщениями с MQTT-брокером
    MQTT_Message = None

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

        # Журнал системы событий
        self.Action = self._Journal_Action()
        # Журнал изменения времени
        self.Time = self._Journal_Time()
        # Журнал сетевых подключений
        self.ServerConnect = self._Journal_ServerConnect()
        # Журнал PPP подключений - Клиент
        self.PPP_ClientConnect = self._Journal_PPP_ClientConnect()
        # Журнал PPP подключений - Сервер
        self.PPP_ServerConnect = self._Journal_PPP_ServerConnect()
        # Журнал входящих вызовов (CSD)
        self.Call = self._Journal_Call()
        # Журнал изменения состояния дискретных входов
        self.DIn_Sens = self._Journal_DIn_Sens()
        # Журнал изменения состояния дискретных входов
        self.DIn_Powerline = self._Journal_DIn_PowerLine()
        # Журнал изменения состояния дискретных входов
        self.DIn_Power = self._Journal_DIn_Power()
        # Журнал изменения состояния дискретных входов
        self.DIn_Charge = self._Journal_DIn_Charge()
        # Журнал изменения состояния дискретных входов
        self.DIn_Open = self._Journal_DIn_Open()
        # 	Журнал авторизации
        self.Auth_JSON = self._Journal_Auth_JSON()
        # 	Журнал перезагрузок
        self.Reset = self._Journal_Reset()
        # 	Журнал хранилища почтовых сообщений
        self.Mail_Message = self._Journal_Mail_Message()
        # 	Журнал отправки почтовых сообщений
        self.Mail_Send = self._Journal_Mail_Send()
        # 	Журнал изменения версии ВПО изделия
        self.Update_Version = self._Journal_Update_Version()
        # Журнал обновления ВПО загрузчика
        self.Update_Loader = self._Journal_Update_Loader()
        # 	Журнал фиксации ответов приборов учета
        self.Meter_Answer = self._Journal_Meter_Answer()
        # 	Журнал хранилища исходящих SMS сообщений
        self.SMS_Message = self._Journal_SMS_Message()
        # 	Журнал отправки SMS
        self.SMS_Send = self._Journal_SMS_Send()
        # 	Журнал приема SMS
        self.SMS_Get = self._Journal_SMS_Get()
        # 	Журнал установки связи с MQTT-брокером
        self.MQTT_Connect = self._Journal_MQTT_Connect()
        # Журнал обмена сообщениями с MQTT-брокером
        self.MQTT_Message = self._Journal_MQTT_Message()

    # Журнал системы событий
    def _Journal_Action(self):
        """
        Журнал системы событий
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_Action import JournalAction
        Action = JournalAction(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Action

    # Журнал изменения времени
    def _Journal_Time(self):
        """
        Журнал изменения времени
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_Time import JournalTime
        Time = JournalTime(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Time

    # Журнал сетевых подключений
    def _Journal_ServerConnect(self):
        """
        Журнал сетевых подключений
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_ServerConnect import JournalServerConnect
        ServerConnect = JournalServerConnect(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return ServerConnect

    # Журнал PPP подключений - Клиент
    def _Journal_PPP_ClientConnect(self):
        """
        Журнал PPP подключений - Клиент
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_PPP_ClientConnect import JournalPPPClientConnect
        PPPClientConnect = JournalPPPClientConnect(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return PPPClientConnect

    # Журнал PPP подключений - Сервер
    def _Journal_PPP_ServerConnect(self):
        """
        Журнал PPP подключений - Сервер
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_PPP_ServerConnect import JournalPPPServerConnect
        PPPServerConnect = JournalPPPServerConnect(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return PPPServerConnect

    # Журнал входящих вызовов (CSD)
    def _Journal_Call(self):
        """
        Журнал входящих вызовов (CSD)
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_Call import JournalCall
        Call = JournalCall(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Call

    # Журнал изменения состояния дискретных входов
    def _Journal_DIn_Sens(self):
        """
        Журнал изменения состояния дискретных входов
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_DIn_Sens import JournalDInSens
        DInSens = JournalDInSens(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return DInSens

    # Журнал изменения состояния дискретных входов
    def _Journal_DIn_PowerLine(self):
        """
        Журнал изменения состояния дискретных входов
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_DIn_PowerLine import JournalDInPowerLine
        DInPowerLine = JournalDInPowerLine(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return DInPowerLine

    # Журнал изменения состояния дискретных входов
    def _Journal_DIn_Power(self):
        """
        Журнал изменения состояния дискретных входов
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_DIn_Power import JournalDInPower
        DInPower = JournalDInPower(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return DInPower

    # Журнал изменения состояния дискретных входов
    def _Journal_DIn_Charge(self):
        """
        Журнал изменения состояния дискретных входов
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_DIn_Charge import JournalDInCharge
        DInCharge = JournalDInCharge(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return DInCharge

    # Журнал изменения состояния дискретных входов
    def _Journal_DIn_Open(self):
        """
        Журнал изменения состояния дискретных входов
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_DIn_Open import JournalDInOpen
        DInOpen = JournalDInOpen(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return DInOpen

    # 	Журнал авторизации
    def _Journal_Auth_JSON(self):
        """
        Журнал авторизации
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_Auth_JSON import JournalAuthJSON
        AuthJSON = JournalAuthJSON(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return AuthJSON

    # 	Журнал перезагрузок
    def _Journal_Reset(self):
        """
        Журнал перезагрузок
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_Reset import JournalReset
        Reset = JournalReset(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Reset

    # 	Журнал хранилища почтовых сообщений
    def _Journal_Mail_Message(self):
        """
        Журнал хранилища почтовых сообщений
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_Mail_Message import JournalMailMessage
        MailMessage = JournalMailMessage(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return MailMessage

    # 	Журнал отправки почтовых сообщений
    def _Journal_Mail_Send(self):
        """
        Журнал отправки почтовых сообщений
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_Mail_Send import JournalMailSend
        MailSend = JournalMailSend(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return MailSend

    # 	Журнал изменения версии ВПО изделия
    def _Journal_Update_Version(self):
        """
        Журнал изменения версии ВПО изделия
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_Update_Version import JournalUpdateVersion
        UpdateVersion = JournalUpdateVersion(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return UpdateVersion

    # Журнал обновления ВПО загрузчика
    def _Journal_Update_Loader(self):
        """
        Журнал обновления ВПО загрузчика
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_Update_Loader import JournalUpdateLoader
        UpdateLoader = JournalUpdateLoader(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return UpdateLoader

    # 	Журнал фиксации ответов приборов учета
    def _Journal_Meter_Answer(self):
        """
        Журнал фиксации ответов приборов учета
        """

        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_Meter_Answer import JournalMeterAnswer
        MeterAnswer = JournalMeterAnswer(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return MeterAnswer

    # 	Журнал хранилища исходящих SMS сообщений
    def _Journal_SMS_Message(self):
        """
        Журнал хранилища исходящих SMS сообщений
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_SMS_Message import JournalSMSMessage
        SMSMessage = JournalSMSMessage(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return SMSMessage

    # 	Журнал отправки SMS
    def _Journal_SMS_Send(self):
        """
        Журнал отправки SMS
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_SMS_Send import JournalSMSSend
        SMSSend = JournalSMSSend(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return SMSSend

    # 	Журнал приема SMS
    def _Journal_SMS_Get(self):
        """
        Журнал приема SMS
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_SMS_Get import JournalSMSGet
        SMSGet = JournalSMSGet(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return SMSGet

    # 	Журнал установки связи с MQTT-брокером
    def _Journal_MQTT_Connect(self):
        """
        Журнал установки связи с MQTT-брокером
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_MQTT_Connect import JournalMQTTConnect
        MQTTConnect = JournalMQTTConnect(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return MQTTConnect

    # Журнал обмена сообщениями с MQTT-брокером
    def _Journal_MQTT_Message(self):
        """
        Журнал обмена сообщениями с MQTT-брокером
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_MQTT_Message import JournalMQTTMessage
        MQTTMessage = JournalMQTTMessage(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return MQTTMessage
