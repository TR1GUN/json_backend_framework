# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 40 СМАРТ - Поле MeterData
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.TemplateUSPD import Template_UM_XX_SMART_MeterData


class UM_40_SMART_MeterData(Template_UM_XX_SMART_MeterData):
    """

    Саб класс который работает с разделом УСПД :  Опрос приборов учета

    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал
    # Опрос приборов учета
    # MeterData = None
    # Опрос приборов учета – Архивные записи
    MeterData_Arch = None
    # Опрос приборов учета – Моментные показатели
    MeterData_Moment = None

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

        self.MeterData_Arch = self._MeterData_Arch()
        self.MeterData_Moment = self._MeterData_Moment()

    # ----->

    def _MeterData_Arch(self):
        """
        Опрос приборов учета – Архивные записи
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterData.MeterData_Arch import MeterDataArch
        MeterDataArch_read = MeterDataArch(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return MeterDataArch_read

    def _MeterData_Moment(self):
        """
        Опрос приборов учета – Моментные показатели
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.MeterData.MeterData_Moment import MeterDataMoment
        MeterDataMoment_read = MeterDataMoment(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return MeterDataMoment_read
