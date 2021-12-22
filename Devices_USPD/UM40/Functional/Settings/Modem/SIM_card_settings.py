# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

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

    def settings_Sim_1(self):
        """
        Получить настройки Sim1
        :return:
        """

        return self._Setting_Sim1

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

    def settings_Sim_2(self):
        """
        Получить настройки Sim2
        :return:
        """

        return self._Setting_Sim2


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки СИМ карт
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

from Service.Template_Functional import TemplateFunctional


class SIM_card(TemplateFunctional):
    """
    Настройки SIM-карт (Pin, APN)

    """
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("SIM_card_settings")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    SettingsSim = SettingsSim()

    # Настройки по умолчанию

    # Настройки сим карт
    _Sim1 = {'id': 1, 'pin': '', 'addr': 'internet.beeline.ru', 'auth': False, 'login': 'beeline',
             'password': 'beeline', 'enable': True}
    _Sim2 = {'id': 2, 'pin': '2527', 'addr': 'internet.beeline.ru', 'auth': True, 'login': 'beeline',
             'password': 'beeline', 'enable': True}

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Настройки SIM-карт (Pin, APN)

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

        # print(self.headers)
        # print(self.cookies)

        # Обьявляем наш класс настроек
        # self.SettingsSim = SettingsSim()

    def read_settings(self):
        """
        Читаем данные - GET
        :return:
        """
        # делаем запрос - получаем ответ
        response = self._request_GET(JSON='')

        return response

    def write_settings(self, data=None):
        """
        Добавляем на запись данные  - POST

        :param data:
        :return:
        """

        if data is None:
            data_settings = self._getting_settings()
            data = {'Settings': data_settings}

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_POST(JSON=data)

        return response

    def rewrite_settings(self, data):
        """
        Перезаписываем данные - PUT
        :param data:
        :return:
        """
        if data is None:
            data_settings = self._getting_settings()
            data = {'Settings': data_settings}

        # Запаковываем
        data = self._coding(data=data)

        # делаем запрос - получаем ответ
        response = self._request_PUT(JSON=data)

        return response

    def delete_settings(self, data=None):
        """
        Удаляем данные - DELETE
        :param data:
        :return:
        """
        # Запаковываем
        if data is not None:
            data = self._coding(data=data)

            # делаем запрос - получаем ответ
            response = self._request_DELETE(JSON=data)
        else:
            # делаем запрос - получаем ответ
            response = self._request_DELETE()

        return response

    # Здесь расположим сервисные функции
    # Первое - Получаем настройки что уже есть

    def _getting_settings(self):

        """

        Получение настроек что задали

        """

        # Пункт первый -  читаем какие настройки у нас есть
        SIM1 = self.SettingsSim.settings_Sim_1()
        SIM2 = self.SettingsSim.settings_Sim_2()

        # ТЕПЕРЬ, если у нас оба сейтинга не заданы , запрашиваем :
        if (SIM1 is None) or (SIM2 is None):
            _Sim1, _Sim2 = self._request_setting()
            # Теперь смотрим точно что необходимо переназначить
            if SIM1 is None:
                # Теперь смотрим что считали
                if _Sim1 is None:
                    SIM1 = self._Sim1
                else:
                    SIM1 = _Sim1
            if SIM2 is None:
                # Теперь смотрим что считали
                if _Sim2 is None:
                    SIM2 = self._Sim2
                else:
                    SIM2 = _Sim2

        # Теперь формируем нужный JSON
        # JSON = {"Settings" : [SIM1, SIM2]}
        JSON = [SIM1, SIM2]
        return JSON

    # Запрос настроек
    def _request_setting(self):
        """
        Здесь запрашиваем нужные нам настройки

        """
        _Sim1 = None
        _Sim2 = None
        try:
            # делаем запрос - получаем ответ
            response = self.read_settings()
            # Теперь вытаскиваем нужное
            if response.get('code') == int(200):
                sim_setting = response.get('data')
                # Теперь заполянем наши переменные
                if sim_setting is not None:

                    print(sim_setting)
                    Settings = sim_setting['Settings']
                    # Теперь перебираем все это
                    for idx in Settings:
                        if idx.get('id') == 1:
                            _Sim1 = idx
                        if idx.get('id') == 2:
                            _Sim2 = idx

        except Exception as e:

            print("При считывании параметров возникла ошибка - " + str(e))

        return _Sim1, _Sim2


# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON
# -------------------------------------------------------------------------------------------------------------
# data = {'Settings': [
#     {'id': 1, 'pin': '', 'addr': 'internet.beeline.ru', 'auth': False, 'login': 'beeline', 'password': 'beeline',
#      'enable': True},
#     {'id': 2, 'pin': '2527', 'addr': 'internet.beeline.ru', 'auth': True, 'login': 'beeline', 'password': 'beeline',
#      'enable': True}]}
# -------------------------------------------------------------------------------------------------------------