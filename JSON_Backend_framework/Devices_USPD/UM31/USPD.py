# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                             Здесь опишем наши классы для работы с разными УСПД
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# импортируем наши классы

from JSON_Backend_framework.Service.TemplateUSPD import Template_USPD

from JSON_Backend_framework.Service.config import headers_protocol_UM31


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                            УМ - 31 СМАРТ
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

class UM_31_SMART(Template_USPD):
    """
    Функционал УМ - 31 СМАРТ

    """
    # Переменные нужные для авторизации
    # Логин
    _Login = 'admin'
    # Пароль
    _Password = 'admin'
    # IP адрес УСПД
    _ip_address = 'localhost'

    # Поля Необходимые для доступа
    # Настройки
    Settings = None

    def __init__(self, Login: str = 'admin', Password: str = 'admin', ip_address=None):
        """
        Функционал УМ - 31 СМАРТ

        :param Login: Логин - стоит значение по умолчанию
        :param Password: Пароль - Стоит значение по умолчанию
        :param ip_address: IP адрес УСПД - Если не заданно - Берется из файла ini
        """
        # Куки - Перед началом работы обнуляем их
        self._cookies = None
        # Состравояем хедерс - необходим для указания протокола
        self._Define_Headers()
        # Определяем логин
        self._Login = str(Login)
        # Определяем пароль
        self._Password = str(Password)

        # Устанавливаем IP адрес
        self._ip_address = str(ip_address)

        # А Теперь - авторизуемся
        self._Authorization()

        # И обновляем функционал
        self._define_functionality()

    # Абгрейд хедерса - указываем протокол в котором работам
    def _Define_Headers(self):
        """
        Это очень важный метод
        """
        from JSON_Backend_framework.Service.Template_Headers import UM_Headers
        self._headers = UM_Headers(UM_Protocol=headers_protocol_UM31.get(self.Name_Protocol_USPD),
                                   Version=headers_protocol_UM31.get(self.Name_Protocol_Version))

    # АВТОРИАЗЦИЯ - должна происходить автоматически - при протухании кукис - перелогиниваться
    def _Authorization(self):
        """
        Метод Авторизации - для УМ 31 смарт
        :return:
        """
        from JSON_Backend_framework.Service.Template_Cookies import UM_Cookies

        self._cookies = UM_Cookies(
                                        Login=self._Login,
                                        Password=self._Password,
                                        IP_address=self._ip_address,
                                        Headers=self._headers,
                                        Auth=True
                                    )
        # # Теперь проверяем что успешно прошли авторизацию
        # from JSON_Backend_framework.Devices_USPD.Authorization import Authorization
        #
        # Authorization_cookie = Authorization(Login=str(self._Login),
        #                                      Password=str(self._Password),
        #                                      ip_address=str(self._ip_address))
        #
        # # Если авториазия была успешна
        #
        # if Authorization_cookie.result_code == 200:
        #     self._cookies = Authorization_cookie.get_cookies()
        # else:
        #     print('Авторизация - не выполнено')
        #
        #     assert Authorization_cookie.result_code == 200, Authorization_cookie.get_result()

    def _define_functionality(self):
        """
        Функция для получения доступа к Функционалу

        :return:
        """
        # Обновляем Настройки
        self._Settings()
        self._StateInfo()
        self._Journal()
        self._Actions()
        self._MeterDeviceManagement()
        self._MeterData()

    def _Settings(self):
        """
        Получаем Класс который работает с настройками УСПД
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Service.USPD_Settings import UM_31_SMART_Settings
        self.Settings = UM_31_SMART_Settings(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    # Состояние Изделия
    def _StateInfo(self):
        """
        Получаем Класс который работает с Информация о состоянии УСПД
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Service.USPD_StateInfo import UM_31_SMART_StateInfo
        self.StateInfo = UM_31_SMART_StateInfo(cookies=self._cookies, headers=self._headers,
                                               ip_address=self._ip_address)

    # ЖУРАНЛЫ
    def _Journal(self):
        """
        Получаем класс который работает с Журналами УСПД
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Service.USPD_Journal import UM_31_SMART_Journal

        self.Journal = UM_31_SMART_Journal(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    # Действия
    def _Actions(self):
        """
        Получаем класс который работает с Действия УСПД
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Service.USPD_Actions import UM_31_SMART_Actions

        self.Action = UM_31_SMART_Actions(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    # Управление Приборами учета
    def _MeterDeviceManagement(self):
        """
        Получаем класс который работает с Действия УСПД
        """
        from JSON_Backend_framework.Devices_USPD.UM31.Service.USPD_MeterDeviceManagement import \
            UM_31_SMART_MeterDeviceManagement

        self.MeterDeviceManagement = UM_31_SMART_MeterDeviceManagement(
            cookies=self._cookies,
            headers=self._headers,
            ip_address=self._ip_address
        )

    # Опрос Приборов Учета
    def _MeterData(self):
        """

        Получаем класс который работает с Действия УСПД

        """

        from JSON_Backend_framework.Devices_USPD.UM31.Service.USPD_MeterData import UM_31_SMART_MeterData

        self.MeterData = UM_31_SMART_MeterData(cookies=self._cookies, headers=self._headers,
                                               ip_address=self._ip_address)
