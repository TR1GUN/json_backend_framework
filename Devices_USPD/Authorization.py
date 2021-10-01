# Здесь опишем класс Авторизации
from Service.Template_Functional import TemplateFunctional


# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                                         Авторизация
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


class Authorization(TemplateFunctional):
    # Шаблон JSON для авторизации
    _data_Authorization = {'login': "admin", 'password': "admin"}
    # URL
    from Devices_USPD.settings import url_path
    _path_url = url_path.get("Authorization")

    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None
    # Куки для авторизации
    _cookies_to_authorization = None
    # IP Адрес

    _ip_address = 'localhost'

    _result = None

    def __init__(self, Login: str = None, Password: str = None, ip_address: str = None):

        # Первое - Получаем айпишник
        ip_address = self._define_IP_address(ip_address=ip_address)

        # Второе - Парсим логин и пароль
        self._parse_Login_and_password(Login=Login, Password=Password)

        # Третье - Производим авторизацию
        # Обнуляем куки
        self._result = None
        self._cookies = None
        self._cookies_to_authorization = None
        # заходим
        self._result = self._Autorization()

    def _define_IP_address(self, ip_address):
        """
        Определяем IP адрес железки

        :param ip_address:
        :return:
        """
        from Service.config import machine_ip
        if ip_address is None:
            ip_address = machine_ip

        ip_address = str(ip_address)

        self._ip_address = ip_address

        return ip_address

    def _parse_Login_and_password(self, Login, Password):
        """
        В Этом методе парсим логин и пароль , чтоб потом задать его на авторизацию

        :param Login:
        :param Password:
        :return:
        """
        # Пункт первый - если у нас логин и пароль стоит в None то парсим из конфига
        from Service.config import USPD_password, USPD_login
        if Login is None:
            Login = USPD_login
        if Password is None:
            Password = USPD_password

        # Теперь вставляем в наши данные для авториазции
        self._data_Authorization['login'] = str(Login)
        self._data_Authorization['password'] = str(Password)

    def _Autorization(self):
        """
        Метод авторизации - Отправляем запрос авторизации - если успешно - то возвращаем куку
        Если нет - Делаем ассерт
        :return:
        """

        data_Authorization_JSON = self._coding(data=self._data_Authorization)
        # Отправляем запрос
        result = self._request_POST(JSON=data_Authorization_JSON)

        return result

    # /// ПЕРЕОПРЕДЕЛЕНЫЙ МЕТОД основного класса - НЕ трогать
    def _parser_request(self, response):
        """
        Считываем нужные данные
        :param response:
        :return: Возвращаем response_dict
        """
        # Код операции
        self.result_code = response.GET_result_code()
        # Текстовые данные , если есть
        self.data = response.GET_data()
        # куки
        self._cookies_to_authorization = response.get_cookies()
        self._cookies = response.get_cookies()
        # headers
        headers = response.get_headers()
        # Общий словарь данных
        response_dict = response.Result()

        return response_dict

    def get_cookies(self):
        """
        Возвращаем куки
        :return:
        """
        return self._cookies

    def get_result(self):
        return self._result



# Authorization(ip_address='http://192.168.0.1/')
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

import requests

# testing_url = 'http://192.168.0.1/'
#
# auth = 'http://192.168.0.1/auth'
#
# json_text = {"login": "admin", "password": "admin"}

# json_text = '{"password": "admin", "login": "admin"}'

# user_agent_val = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
# # login = 'http://192.168.0.1/login'
# #
# # json_text = {'password': 'admin', 'login': 'admin'}
# # response = requests.get(login)
# # print(response.text)
# Referer = 'http://192.168.0.1/login'
# headers = {
#     'User-Agent': user_agent_val,
#     'Referer': 'http://192.168.0.1/login',
#     'Host': '192.168.0.1',
#     # 'Connection': keep-alive
#     'Accept': '*/*',
#     'Content-type': 'application/json',
#     'Origin': 'http://192.168.0.1',
#     # 'Cookie': 'sessionid=16349148992619061200'
# }
#
# ip = "http://192.168.0.1/"
# login = "login"
#
# url_login = ip + login

# response = requests.get(url_login)
# print(response.cookies.get(name='sessionid'))
# print(response.headers)
#

# json_text = '{"password":"admin","login":"admin"}'
# json_ = {"password": "admin", "login": "admin"}
# testing_url = 'http://192.168.0.1/'
# print('---->', testing_url + 'auth')
# import json
#
# json_text = {"password": "admin", "login": "admin"}
# json_text = json.dumps(json_text)
# # теперь убираем все пробелы
#
#
# # testing_url = 'http://192.168.202.143/'
# testing_url = 'http://192.168.0.1/'
# print('---->', testing_url + 'auth')

# теперь убираем все пробелы

# import json
#
# # ----->
# json_text = {"password": "admin", "login": "admin"}
# json_text = json.dumps(json_text)
#
# json_text = json_text.replace(" ", '')
#
# response = requests.post(testing_url + 'auth', data=json_text, headers=headers)
# print(response)
# print(response.cookies)
#
# Забираем куку

# cookies = response.cookies
# tcp = 'settings/servers/tcp'
#
# response = requests.get(testing_url + 'state/network', cookies=cookies)
#
# print(response)
# print(response.text)


# session = requests.Session()
# r = session.get(Referer, headers = {
#                 'User-Agent': user_agent_val})
#
# session.headers.update({'Referer':Referer})
# session.headers.update({'User-Agent':user_agent_val})
# _xsrf = session.cookies.get('_xsrf', domain=testing_url)
#
# print(r.headers)
# response = requests.post(auth, timeout=2,
#                          data=json_text,
#                          headers=headers
#                          )
# print(response.text)

# cookies = response.cookies
# print(cookies)
# response = requests.get(testing_url + 'state/network')
# # response = requests.get(testing_url + 'settings/templates/meter', cookies=cookies)
# print(response)


# from requests.auth import HTTPBasicAuth
# # указываем параметры аутентификации
# auth = HTTPBasicAuth('admin', 'admin')
# print(auth)
# response = requests.post('http://192.168.0.1/auth',data={'password': 'admin', 'login': 'admin'}, auth=auth)
# print(response)
#
# response = requests.get('http://192.168.0.1/state/network', auth=auth)
# print(response)
