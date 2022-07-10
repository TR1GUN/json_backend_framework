# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Чтение Данных счетчиков
#                                     Основной класс для взаимодействия
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterData.Measures_Journal import MeterData_Journal
from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterData.Measures_Moment import MeterData_Moment
from JSON_Backend_framework.Devices_USPD.UM31.Functional.MeterData.Measures_Archive import MeterData_Arch
# -------------------------------------------------------------------------------------------------------------


class MeterData_MeasureRead:
    """
    Чтение Данных счетчиков

    """

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    _ip_address = None
    # Журналы
    Journal = None

    # Данные со счетчика - Моментные показатели
    MeterData_Moment = None
    # Данные со счетчика - Архивные показатели
    MeterData_Arch = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Чтение Данных счетчиков

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

        self._define_functional()

    def _define_functional(self):
        """
        В этом методе делаем самое важное - определяем функционал работы по отраслям в полях этого класса

        :return:
        """

        self.Journal = MeterData_Journal(cookies=self._cookies,
                                         headers=self._headers,
                                         ip_address=self._ip_address)
        self.MeterData_Moment = MeterData_Moment(cookies=self._cookies,
                                                 headers=self._headers,
                                                 ip_address=self._ip_address)
        self.MeterData_Arch = MeterData_Arch(cookies=self._cookies,
                                             headers=self._headers,
                                             ip_address=self._ip_address)
