# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Настройки СИМ карт
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.Settings.Modem.Template_SIM_card_settings import TemplateSIM
from JSON_Backend_framework.Service.TemplateDecorator import print_log_use_GET_data
from JSON_Backend_framework.FormJSON.UM40.Settings.Modem.JSON_Construct_Settings_SIM import SettingsSim
# -------------------------------------------------------------------------------------------------------------


class SIM_card(TemplateSIM):
    """
    Настройки SIM-карт (Pin, APN)

    """
    # URL
    # from Devices_USPD.settings import url_path
    # _path_url = url_path.get("Settings_SIM")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    # Общие настройки
    Settings = None

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
        # Обнуляем
        self._define_JSON()

    def _define_JSON(self):
        """
        Здесь Сбрасываем настройки
        """
        # Сбрасываем настройки
        self.Settings = SettingsSim()

    def _getting_settings(self):

        """

        Получение настроек что задали

        """

        # Пункт первый -  читаем какие настройки у нас есть
        SIM = self.Settings.get_settings_Sim()

        SIM1 = None
        SIM2 = None
        SIM = SIM.get(self._Settings_name)
        for i in SIM:
            if i.get('id') == 1:
                SIM1 = i
            if i.get('id') == 2:
                SIM2 = i

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
        # Обнуляем
        self._define_JSON()
        # Теперь формируем нужный JSON
        # JSON = {"Settings" : [SIM1, SIM2]}
        JSON = [SIM1, SIM2]
        return JSON

    # Запрос настроек
    @print_log_use_GET_data
    def _request_setting(self):
        """
        Здесь запрашиваем нужные нам настройки

        """
        _Sim1 = None
        _Sim2 = None
        try:
            # делаем запрос - получаем ответ
            response = self.Read_Settings()
            # Теперь вытаскиваем нужное
            if response.get('code') == int(200):
                sim_setting = response.get('data')
                # Теперь заполянем наши переменные
                if sim_setting is not None:
                    Settings = sim_setting[self._Settings_name]
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
