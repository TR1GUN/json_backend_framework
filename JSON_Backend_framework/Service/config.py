# import configparser
# import os
# # Здесь парсим наш конфиг тестов
#
# # Здесь расположим парсер наших данных - Это очень важно
# # ---------------------------------------- Получение информации об ОС ---------------------------------------------
# def get_platform():
#     """
#     Получение информации о системе - Это важно
#     :return:
#     """
#
#     import platform
#
#     # получаем нашу систему -
#     platform_os = platform.system()
#
#     # print(platform_os)
#
#     # if 'Windows' in platform_os:
#     #     platform_os = 'Windows'
#     # else:
#     #     platform_os = 'Linux'
#     #
#     # return platform_os
# # from Service import get_platform
#
# # получаем нашу систему -
# platform_os = get_platform()
# # print(platform_os)
#
#
#
#
# # # ----------------------------------------------------------------------------
# # # path ='/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
# path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
# # print(path)
# settings = '../settings.ini'
# path = os.path.join(path, settings)
# # print(path)
# # # настройки берем из конфига
# parser = configparser.ConfigParser()
#
#
# parser.read(path)
# # # -----------------------------------------------------------------------------
# # #                             САМИ НАСТРОЙКИ
# # # -----------------------------------------------------------------------------
# # dbpath = parser[platform_os]['dbpath']
# # IP_address = parser[platform_os]['dbpath']
# # IP_port = parser[platform_os]['dbpath']


# СТАРОЕ ---------------->
# machine_ip = parser['Test']['IP_address']
# USPD_login = parser['Test']['USPD_login']
# USPD_password = parser['Test']['USPD_password']

# user_login = parser['Test']['user_login']
# user_password = parser['Test']['user_password']
# address_ssh = parser['Test']['address_ssh']
# domain = parser['Test']['domain']
# print(machine_ip)

from JSON_Backend_framework import Machine_IP, Login, Password

machine_ip = Machine_IP
USPD_login = Login
USPD_password = Password


# АВТОПАРСЕР settings.ini
def search_settings():
    """

    """
    # Первое - Инициализируем файл
    import os, configparser
    path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
    settings = '../settings.ini'
    path = os.path.join(path, settings)
    print('--->', path)
    parser = configparser.ConfigParser()


    parser.read(path)
    # # -----------------------------------------------------------------------------
    # #                             САМИ НАСТРОЙКИ
    # # -----------------------------------------------------------------------------
    settings_section = 'Test'
    machine_ip = parser[settings_section]['IP_address']
    USPD_login = parser[settings_section]['USPD_login']
    USPD_password = parser[settings_section]['USPD_password']
    print('--->', machine_ip)
    print('--->', USPD_login)
    print('--->', USPD_password)

search_settings()