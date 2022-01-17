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
    # Журнал изменения времени
    Time = None
    # Журнал фиксации ответов приборов учета
    Meter_answer = None

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

        self.Meter_answer = self._Journal_Meter_answer()
        self.Time = self._Journal_Time()

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

    def _Journal_Meter_answer(self):
        """
        Журнал Ответов счетчика

        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Journal.Journal_Meter_answer import JournalMeterAnswer
        MeterAnswer = JournalMeterAnswer(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return MeterAnswer
