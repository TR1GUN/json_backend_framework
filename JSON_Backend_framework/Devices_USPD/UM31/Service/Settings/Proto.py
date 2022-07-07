# -------------------------------------------------------------------------------------------------------------
#                                     Поле Settings.Proto
# -------------------------------------------------------------------------------------------------------------

class SettingsProto:
    _cookies = None
    _headers = None
    _ip_address = None

    # Настройки http авторизации
    JSON_Auth = None
    # Настройки авторизации текстового протокола
    Text_Auth = None
    # Настройки авторизации протокола RTU-327
    RTU_Auth = None
    # Настройки выдачи данных текстового протокола
    Text_Data = None
    # Настройка почтовых сообщений текстового протокола
    Text_Mail = None

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
        self.JSON_Auth = self._Proto_JSON_Auth()
        self.Text_Auth = self._Proto_Text_Auth()
        self.RTU_Auth = self._Proto_RTU_Auth()
        self.Text_Data = self._Proto_Text_Data()
        self.Text_Mail = self._Proto_Text_Mail()

    # Здесь генерируем сам функционал :
    # Настройки http авторизации
    def _Proto_JSON_Auth(self):
        """
        Настройки http авторизации
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Proto.Proto_JSON_auth import ProtoJSONAuth
        JSONAuth = ProtoJSONAuth(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return JSONAuth

    # Настройки авторизации текстового протокола
    def _Proto_Text_Auth(self):
        """
        Настройки авторизации текстового протокола
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Proto.Proto_TEXT_auth import ProtoTextAuth
        TextAuth = ProtoTextAuth(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return TextAuth

    # Настройки авторизации протокола RTU-327
    def _Proto_RTU_Auth(self):
        """
        Настройки авторизации протокола RTU-327
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Proto.Proto_RTU_auth import ProtoRTUAuth
        RTUAuth = ProtoRTUAuth(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return RTUAuth

    # Настройки выдачи данных текстового протокола
    def _Proto_Text_Data(self):
        """
        Настройки выдачи данных текстового протокола
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Proto.Proto_TEXT_data import ProtocolTextData
        TextData = ProtocolTextData(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return TextData

    # Настройка почтовых сообщений текстового протокола
    def _Proto_Text_Mail(self):
        """
        Настройка почтовых сообщений текстового протокола
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Functional.Settings.Proto.Proto_TEXT_data import ProtocolTextData
        TextData = ProtocolTextData(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )
        return TextData

