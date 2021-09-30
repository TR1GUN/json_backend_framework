# Здесь опишем класс Авторизации

class Authorization:
    url = '/auth'
    data_Authorization = {'login': "admin", 'password': "admin"}

    def __init__(self):
        self.Autorization()

    def Autorization(self):
        from Service.Request_POST import POST

        result = POST(url=self.url, data=self.data_Authorization).Result()
        print(result)

        import requests


import requests

testing_url = 'http://192.168.0.1/'

auth = 'http://192.168.0.1/auth'

json_text = {"login": "admin", "password": "admin"}

# json_text = '{"password": "admin", "login": "admin"}'

user_agent_val = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
# login = 'http://192.168.0.1/login'
#
# json_text = {'password': 'admin', 'login': 'admin'}
# response = requests.get(login)
# print(response.text)
Referer = 'http://192.168.0.1/login'
headers = {
    'User-Agent': user_agent_val,
    # 'Referer': 'http://192.168.0.1/login',
    'Host': '192.168.0.1',
    # 'Connection': keep-alive
    'Accept': '*/*',
    'Content-type': 'application/json',
    'Origin': 'http://192.168.0.1',
    # 'Cookie': 'sessionid=16349148992619061200'
}

ip = "http://192.168.0.1/"
login = "login"

url_login = ip + login

# response = requests.get(url_login)
# print(response.cookies.get(name='sessionid'))
# print(response.headers)
#

# json_text = '{"password":"admin","login":"admin"}'
json_ = {"password": "admin", "login": "admin"}
testing_url = 'http://192.168.0.1/'
print('---->', testing_url + 'auth')
import json

json_text = {"password": "admin", "login": "admin"}
json_text = json.dumps(json_text)
# теперь убираем все пробелы


response = requests.post(testing_url + 'auth', data=json_text, headers=headers)
print(response)
print(response.cookies)
#
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
