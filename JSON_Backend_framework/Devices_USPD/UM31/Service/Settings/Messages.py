# -------------------------------------------------------------------------------------------------------------
#                                     Поле Settings.Messages
# -------------------------------------------------------------------------------------------------------------

class SettingsMessages:
    _cookies = None
    _headers = None
    _ip_address = None

    # Адресная книга
    Address = None
    # Сообщения пользователя
    Messages_Custom = None
    # Сообщения с данными приборов учета
    Messages_Meter = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        self._cookies = cookies
        self._headers = headers
        self._ip_address = ip_address
        # Обновляем функционал
        # ---->
        self._define_functionality()

    def _define_functionality(self):
        """
        Получение функционала
        """
        # Адресная книга
        self.Address = self._Messages_Address()
        # Сообщения пользователя
        self.Messages_Custom = self._Messages_Custom()
        # Сообщения с данными приборов учета
        self.Messages_Meter = self._Messages_Meter()

    # Здесь генерируем сам функционал :

    # Адресная книга
    def _Messages_Address(self):
        """
        Адресная книга
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Messages.Adderess import Address
        Address_Messages = Address(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Address_Messages

    # Сообщения пользователя
    def _Messages_Custom(self):
        """
        Сообщения пользователя
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Messages.Messages_custom import MessagesCustom
        Custom = MessagesCustom(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Custom

    # Сообщения с данными приборов учета
    def _Messages_Meter(self):
        """
        Сообщения с данными приборов учета
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Messages.Messages_meter import MessagesMeter
        Meter = MessagesMeter(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return Meter
