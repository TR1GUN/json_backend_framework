# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 40 СМАРТ - Поле State
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from Service.TemplateUSPD import Template_UM_XX_SMART_State


class UM_40_SMART_StateInfo(Template_UM_XX_SMART_State):
    """
    Саб класс который работает с разделом УСПД :  Информация о состоянии изделия
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал
    #   Состояние линий питания интерфейсов
    DOut = None

    # 	Текущее время
    Time = None

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

        self.DOut = self._State_DOut()
        self.Time = self._State_Time()

    def _State_DOut(self):
        """
        Состояние линий питания интерфейсов
        """
        from Devices_USPD.UM40.Functional.InfoState.State_DOut import StateDOut
        DOut = StateDOut(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return DOut

    def _State_Time(self):
        """
        Текущее время

        """
        from Devices_USPD.UM40.Functional.InfoState.Time import StateTime
        Time = StateTime(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Time


