# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Точка Входа в Обвертку
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

class USPD:

    def __init__(self):
        """
        Пока работает через статик методы
        """

    @staticmethod
    def UM_40_Smart():
        """

        :return:
        """
        from Devices_USPD.Devices import UM_40_SMART

        return UM_40_SMART(ip_address=None)

    @staticmethod
    def UM_31_Smart():
        from Devices_USPD.Devices import UM_31_SMART

        return UM_31_SMART(Login='admin', Password='admin', ip_address=None)



SMART = USPD.UM_40_Smart()

# SMART.Ethernet_settings()
print(SMART)