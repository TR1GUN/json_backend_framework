# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
#                              Информация о конфигурации системы
# -------------------------------------------------------------------------------------------------------------
# Импортируем Шаблон взаимодействия

from JSON_Backend_framework.Service.Template_Devices_Functions.State.Template_State_System import TemplateStateSystem

# -------------------------------------------------------------------------------------------------------------


class StateSystem(TemplateStateSystem):
    """
    Информация о конфигурации системы
    """
    # хедерс - Иногда нужен
    _headers = None
    # куки
    _cookies = None

    def __init__(self, cookies=None, headers=None, ip_address=None):
        """
        Информация о конфигурации системы

        :param cookies:
        :param headers:
        """
        if cookies is not None:
            self._cookies = cookies
        if headers is not None:
            self._headers = headers

        if ip_address is not None:
            self._ip_address = ip_address

# -------------------------------------------------------------------------------------------------------------
#                                     ПРИМЕР JSON - Здесь только чтение
# -------------------------------------------------------------------------------------------------------------
# {
# 	"fw":"1.2.1234",
# 	"bl":"1.2.1234",
# 	"SystemInfo":{
# 		"MODEL":"40",
# 		"REV":"0001",
# 		"SN":"123456789012",
# 		"DATE":"2018-06-13T17:07:48+03:00",
# 		"DF":[
# 			{
# 				"TYPE":"AT26DF321",
# 				"NUM":1
# 			}
# 		],
# 		"BAT":"3.7V,1800mAh",
# 		"IF":[
# 			{
# 				"TYPE":"RS485",
# 				"NUM":1
# 			}
# 		],
# 		"MAC":"00:50:C2:ED:A0:01",
# 		"MAIN_PWR":"220/9",
# 		"MODEM":"UG95E(NAR01A09E1G)"
# 	}
# }
# -------------------------------------------------------------------------------------------------------------
