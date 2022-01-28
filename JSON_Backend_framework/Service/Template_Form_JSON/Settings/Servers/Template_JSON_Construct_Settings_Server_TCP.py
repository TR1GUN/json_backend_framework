# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                               Настройки TCP-серверов
# -------------------------------------------------------------------------------------------------------------

# Класс для добавления своих серверов
class TemplateSettingsServer:
    _Server_list = []

    # Сервера что возможны :

    # def __init__(self):
    #     self._Server_list = []
    # Имя поля настроек
    _Settings_name = 'Settings'

    def get_servers(self):
        """
        Отдаем наши введенные порты

        """
        # Имя поля настроек
        return {self._Settings_name: self._Server_list}

    def delete_server_for_port(self, ports: (int, list)):

        if type(ports) is int:
            ports = [ports]

        # Образовываем новый список
        Server_list = []
        # Теперь проходимся по нашему списку и удаляем если есть соответствия
        for setting in self._Server_list:
            if setting.get('port') not in ports:
                Server_list.append(setting)

        # Переопредлеляем
        self._Server_list = Server_list
