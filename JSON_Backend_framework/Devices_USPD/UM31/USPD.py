# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                             Здесь опишем наши классы для работы с разными УСПД
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# импортируем наши классы

from JSON_Backend_framework.Service.TemplateUSPD import Template_USPD


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

    # АВТОРИАЗЦИЯ - должна происходить автоматически - при протухании кукис - перелогиниваться
    def _Authorization(self):
        """
        Метод Авторизации - для УМ 31 смарт
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.Authorization import Authorization

        Authorization_cookie = Authorization(Login=str(self._Login),
                                             Password=str(self._Password),
                                             ip_address=str(self._ip_address))

        # Если авториазия была успешна

        if Authorization_cookie.result_code == 200:
            self._cookies = Authorization_cookie.get_cookies()
        else:
            print('Авторизация - не выполнено')

            assert Authorization_cookie.result_code == 200, Authorization_cookie.get_result()

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
        pass
        # from JSON_Backend_framework.Devices_USPD.UM40.Service.USPD_Settings import UM_40_SMART_Settings
        # self.Settings = UM_40_SMART_Settings(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    # Состояние Изделия
    def _StateInfo(self):
        """
        Получаем Класс который работает с Информация о состоянии УСПД
        :return:
        """
        pass
        # from JSON_Backend_framework.Devices_USPD.UM40.Service.USPD_StateInfo import UM_40_SMART_StateInfo
        # self.StateInfo = UM_40_SMART_StateInfo(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    # ЖУРАНЛЫ
    def _Journal(self):

        """
        Получаем класс который работает с Журналами УСПД
        """
        pass
        # from JSON_Backend_framework.Devices_USPD.UM40.Service.USPD_Journal import UM_40_SMART_Journal
        #
        # self.Journal = UM_40_SMART_Journal(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    # Действия
    def _Actions(self):

        """
        Получаем класс который работает с Действия УСПД
        """
        pass
        # from JSON_Backend_framework.Devices_USPD.UM40.Service.USPD_Actions import UM_40_SMART_Actions
        #
        # self.Action = UM_40_SMART_Actions(cookies=self._cookies, headers=self._headers, ip_address=self._ip_address)

    # Управление Приборами учета
    def _MeterDeviceManagement(self):

        """
        Получаем класс который работает с Действия УСПД
        """
        pass

        # from JSON_Backend_framework.Devices_USPD.UM40.Service.USPD_MeterDeviceManagement import UM_40_SMART_MeterDeviceManagement
        #
        # self.MeterDeviceManagement = UM_40_SMART_MeterDeviceManagement(
        #                                                                 cookies=self._cookies,
        #                                                                 headers=self._headers,
        #                                                                 ip_address=self._ip_address
        #                                                                )

    # Опрос Приборов Учета
    def _MeterData(self):

        """

        Получаем класс который работает с Действия УСПД

        """
        pass

        # from JSON_Backend_framework.Devices_USPD.UM40.Service.USPD_MeterData import UM_40_SMART_MeterData
        #
        # self.MeterData = UM_40_SMART_MeterData(cookies=self._cookies, headers=self._headers,ip_address=self._ip_address)