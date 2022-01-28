# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                               Настройки SIM карт
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------
# Настройки сим карт - Добавление
class SettingsSim:
    """

    Итак - Здесь заполняем настройки

    """

    _Setting_Sim1 = None
    _Setting_Sim2 = None

    _Settings = None
    # Имя поля настроек
    _Settings_name = 'Settings'

    def __init__(self):
        self._Setting_Sim1 = None
        self._Setting_Sim2 = None

    def added_SIM_1(self, pin: int = 1234, enable: bool = True, address: str = 'e.rustatic.beelin', auth: bool = True,
                    login: str = 'beeline', password: str = 'beeline'):
        """
        Настройки SIM 1

        :param pin: - int - PIN-код SIM-карты, 4 цифры
        :param enable: - bool - Разрешение подключения к точке доступа
        :param address: - str - Адрес точки доступа
        :param auth: - bool - Необходимость авторизации
        :param login: - str - Логин
        :param password: - str - Пароль
        :return:
        """

        _Setting_Sim1 = \
            {
                "id": 1,
                "pin": pin,
                "enable": enable,
                "addr": address,
                "auth": auth,
                "login": login,
                "password": password
            }

        self._Setting_Sim1 = _Setting_Sim1

    def remove_Sim_1(self):
        """
        Удаление настроек Sim1, что ввели
        :return:
        """

        self._Setting_Sim1 = None

    # def settings_Sim_1(self):
    #     """
    #     Получить настройки Sim1
    #     :return:
    #     """
    #
    #     return self._Setting_Sim1

    def added_SIM_2(self, pin: int = 1234, enable: bool = True, address: str = 'e.rustatic.beelin', auth: bool = True,
                    login: str = 'beeline', password: str = 'beeline'):
        """
        Настройки SIM 2

        :param pin: - int - PIN-код SIM-карты, 4 цифры
        :param enable: - bool - Разрешение подключения к точке доступа
        :param address: - str - Адрес точки доступа
        :param auth: - bool - Необходимость авторизации
        :param login: - str - Логин
        :param password: - str - Пароль
        :return:
        """

        _Setting_Sim2 = \
            {
                "id": 2,
                "pin": pin,
                "enable": enable,
                "addr": address,
                "auth": auth,
                "login": login,
                "password": password
            }

        self._Setting_Sim2 = _Setting_Sim2

    def remove_Sim_2(self):
        """
        Удаление настроек Sim2, что ввели
        :return:
        """

        self._Setting_Sim2 = None

    # def settings_Sim_2(self):
    #     """
    #     Получить настройки Sim2
    #     :return:
    #     """
    #
    #     return self._Setting_Sim2

    def get_settings_Sim(self):
        """
        Получить настройки Sim
        :return:
        """
        Settings = []
        if self._Setting_Sim1 is not None:
            Settings.append(self._Setting_Sim1)

        if self._Setting_Sim2 is not None:
            Settings.append(self._Setting_Sim2)

        return {self._Settings_name: Settings}
