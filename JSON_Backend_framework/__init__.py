# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Точка Входа в Обвертку
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
Machine_IP = '192.168.202.143'
Login = 'admin'
Password = 'admin'


class USPD:

    def __init__(self):
        """
        Пока работает через статик методы
        """

    @staticmethod
    def UM_40_Smart(ip_address=None):
        """
         Работа с Функционалом УМ-40 SMART
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM40.USPD import UM_40_SMART

        return UM_40_SMART(ip_address=ip_address)

    @staticmethod
    def UM_31_Smart(Login='admin', Password='admin', ip_address=None):
        """
        Работа с Функционалом УМ-31 SMART

        :param Login: ЛОГИН - значение по умолчанию - admin
        :param Password: ПАРОЛЬ - значение по умолчанию - admin
        :param ip_address: IP адресс - По умолчанию адрес берется из конфига
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.USPD import UM_31_SMART

        return UM_31_SMART(Login=Login, Password=Password, ip_address=ip_address)


