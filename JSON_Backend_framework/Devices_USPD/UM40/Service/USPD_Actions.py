# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 40 СМАРТ - Поле Actions
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
from JSON_Backend_framework.Service.TemplateUSPD import Template_UM_XX_SMART_Actions


class UM_40_SMART_Actions(Template_UM_XX_SMART_Actions):
    """
    Саб класс который работает с разделом УСПД :  : Действия
    """

    _cookies = None
    _headers = None
    _ip_address = None

    # Функционал
    # Перезагрузка
    Restart = None

    # Установка времени – Системное время устройства
    Time_Set = None
    # # Синхронизация времени (SNTP)
    # Time_Sync = None
    # # Поверка внешних ЧРВ
    # Time_Check = None
    # # Обновление загрузчика
    # Update_Loader = None
    # # Очистка логического диска
    # Disk_Clear = None
    # # Синхронизация хранилища данных приборов учета
    # Storage_Sync = None

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


        # Перезагрузка
        self.Restart = self._Actions_Restart()
        # Установка времени – Системное время устройства
        self.Time_Set = self._Actions_Time_Set()
        # # Синхронизация времени (SNTP)
        # self.Time_Sync = self._Actions_Time_Sync()
        # # Поверка внешних ЧРВ
        # self.Time_Check = self._Actions_Time_Check()
        # # Обновление загрузчика
        # self.Update_Loader = self._Actions_Update_Loader()
        # # Очистка логического диска
        # self.Disk_Clear = self._Actions_Disk_Clear()
        # # Синхронизация хранилища данных приборов учета
        # self.Storage_Sync = self._Actions_Storage_Sync()

    # Перезагрузка
    def _Actions_Restart(self):
        """
        Перезагрузка
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Action.Action_Device_Restart import ActionDeviceRestart
        DeviceRestart = ActionDeviceRestart(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return DeviceRestart

    # Установка времени – Системное время устройства
    def _Actions_Time_Set(self):
        """
        Установка времени – Системное время устройства
        """
        from JSON_Backend_framework.Devices_USPD.UM40.Functional.Action.Action_Time_Set import ActionTimeSet
        TimeSet = ActionTimeSet(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return TimeSet
    #
    # # Синхронизация времени (SNTP)
    # def _Actions_Time_Sync(self):
    #     """
    #     Синхронизация времени (SNTP)
    #     """
    #     from JSON_Backend_framework.Devices_USPD.UM40.Functional.Action.Action_Time_Sync import ActionTimeSync
    #     TimeSync = ActionTimeSync(
    #         cookies=self._cookies,
    #         headers=self._headers,
    #         ip_address=self._ip_address
    #     )
    #     return TimeSync
    #
    # # Поверка внешних ЧРВ
    # def _Actions_Time_Check(self):
    #     """
    #     Поверка внешних ЧРВ
    #     """
    #     from JSON_Backend_framework.Devices_USPD.UM40.Functional.Action.Action_Time_Check import ActionTimeCheck
    #     TimeCheck = ActionTimeCheck(
    #         cookies=self._cookies,
    #         headers=self._headers,
    #         ip_address=self._ip_address
    #     )
    #     return TimeCheck
    #
    # # Обновление загрузчика
    # def _Actions_Update_Loader(self):
    #     """
    #     Обновление загрузчика
    #     """
    #     from JSON_Backend_framework.Devices_USPD.UM40.Functional.Action.Action_Update_Loader import ActionLoaderUpdate
    #     LoaderUpdate = ActionLoaderUpdate(
    #         cookies=self._cookies,
    #         headers=self._headers,
    #         ip_address=self._ip_address
    #     )
    #     return LoaderUpdate
    #
    # # Очистка логического диска
    # def _Actions_Disk_Clear(self):
    #     """
    #     Очистка логического диска
    #     """
    #     from JSON_Backend_framework.Devices_USPD.UM40.Functional.Action.Action_Disk_Clear import ActionDiskClear
    #     DiskClear = ActionDiskClear(
    #         cookies=self._cookies,
    #         headers=self._headers,
    #         ip_address=self._ip_address
    #     )
    #     return DiskClear
    #
    # # Синхронизация хранилища данных приборов учета
    # def _Actions_Storage_Sync(self):
    #     """
    #     Синхронизация хранилища данных приборов учета
    #     """
    #     from JSON_Backend_framework.Devices_USPD.UM40.Functional.Action.Action_Storage_Sync import ActionStorageSync
    #     StorageSync = ActionStorageSync(
    #         cookies=self._cookies,
    #         headers=self._headers,
    #         ip_address=self._ip_address
    #     )
    #     return StorageSync
