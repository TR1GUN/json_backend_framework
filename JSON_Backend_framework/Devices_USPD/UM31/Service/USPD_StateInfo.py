# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 31 СМАРТ - Поле State
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.TemplateUSPD import Template_UM_XX_SMART_State


class UM_31_SMART_StateInfo(Template_UM_XX_SMART_State):
    """
    Саб класс который работает с разделом УСПД :  Информация о состоянии изделия
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал
    #   Состояние линий питания интерфейсов
    DOut = None
    #   Состояние дискретных входов
    DIn = None
    #   Состояние аналоговых входов
    AIn = None
    # Ожидаемое время срабатывания расписаний
    Scheduler = None
    # 	Состояние последовательных интерфейсов
    UART = None
    #   Состояние сетевых подключений
    Network = None
    # 	Состояние сокетов
    Socket = None
    # 	Состояние микросхем памяти
    DataFlash = None
    # 	Состояние файловой системы
    FileSystem = None
    # 	Состояние модема
    Modem = None
    # 	Состояние операционной системы
    OS = None
    # 	Состояние таблицы приборов учета
    MeterTable = None
    # 	Текущее время
    Time = None
    # Информация о конфигурации системы
    System = None

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

        #   Состояние линий питания интерфейсов
        self.DOut = self._State_DOut()
        #   Состояние дискретных входов
        self.DIn = self._State_DIn()
        #   Состояние аналоговых входов
        self.AIn = self._State_AIn()
        # Ожидаемое время срабатывания расписаний
        self.Scheduler = self._State_Scheduler()
        # 	Состояние последовательных интерфейсов
        self.UART = self._State_UART()
        #   Состояние сетевых подключений
        self.Network = self._State_Network()
        # 	Состояние сокетов
        self.Socket = self._State_Socket()
        # 	Состояние микросхем памяти
        self.DataFlash = self._State_DataFlash()
        # 	Состояние файловой системы
        self.FileSystem = self._State_FileSystem()
        # 	Состояние модема
        self.Modem = self._State_Modem()
        # 	Состояние операционной системы
        self.OS = self._State_OS()
        # 	Состояние таблицы приборов учета
        self.MeterTable = self._State_MeterTable()
        # 	Текущее время
        self.Time = self._State_Time()
        # Информация о конфигурации системы
        self.System = self._State_System()

    #   Состояние линий питания интерфейсов
    def _State_DOut(self):
        """
        Состояние линий питания интерфейсов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_DOut import StateDOut
        DOut = StateDOut(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return DOut

    #   Состояние дискретных входов
    def _State_DIn(self):
        """
        Состояние дискретных входов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_DIn import StateDIn
        DIn = StateDIn(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return DIn

    #   Состояние аналоговых входов
    def _State_AIn(self):
        """
        Состояние аналоговых входов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_AIn import StateAIn
        AIn = StateAIn(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return AIn

    # Ожидаемое время срабатывания расписаний
    def _State_Scheduler(self):
        """
        Ожидаемое время срабатывания расписаний
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_Scheduler import StateScheduler
        Scheduler = StateScheduler(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Scheduler

    # 	Состояние последовательных интерфейсов
    def _State_UART(self):
        """
        Состояние последовательных интерфейсов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_UART import StateUART
        UART = StateUART(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return UART

    #   Состояние сетевых подключений
    def _State_Network(self):
        """
        Состояние сетевых подключений
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_Network import StateNetwork
        Network = StateNetwork(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Network

    # 	Состояние сокетов
    def _State_Socket(self):
        """
        Состояние сокетов
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_Socket import StateSocket
        Socket = StateSocket(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Socket

    # 	Состояние микросхем памяти
    def _State_DataFlash(self):
        """
        Состояние микросхем памяти
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_DataFlash import StateDataFlash
        DataFlash = StateDataFlash(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return DataFlash

    # 	Состояние файловой системы
    def _State_FileSystem(self):
        """
        Состояние файловой системы

        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_FileSystem import StateFileSystem
        FileSystem = StateFileSystem(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return FileSystem

    # 	Состояние модема
    def _State_Modem(self):
        """
        Состояние модема
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_Modem import StateModem
        Modem = StateModem(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Modem

    # 	Состояние операционной системы
    def _State_OS(self):
        """
        Состояние операционной системы
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_OS import StateOS
        OS_USPD = StateOS(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return OS_USPD

    # 	Состояние таблицы приборов учета
    def _State_MeterTable(self):
        """
        Состояние таблицы приборов учета
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_MeterTable import StateMeterTable
        MeterTable = StateMeterTable(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return MeterTable

    # 	Текущее время
    def _State_Time(self):
        """
        Текущее время
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_Time import StateTime
        Time = StateTime(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Time

    # Информация о конфигурации системы
    def _State_System(self):
        """
        Информация о конфигурации системы
        :return:
        """

        from JSON_Backend_framework.Devices_USPD.UM31.Functional.InfoState.State_System import StateSystem
        System = StateSystem(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return System
