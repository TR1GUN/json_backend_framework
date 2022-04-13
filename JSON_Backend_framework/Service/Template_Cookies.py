# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# Здесь опишем класс наших Кукис и Авторизации что б была если чо
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

class UM_Cookies:

    """
    Этот класс отвечает за куки в том или ином их виде -
    Что здесь производиться - Авторизация
    Хранение Куки
    """
    # Само значение Куки
    cookie_value = None
    # Логин
    Login = ""
    # Пароль
    Password = ""
    # IP адрес
    IP_Address = ""
    # Наш Хэдерс
    Headers = None

    def __init__(self, Login : str, Password : str , IP_address : str , Headers = None, Auth : bool = False):
        """
        Здесь храниться то что нам так необходимо -
        :param Login:  - str  - Наш логин
        :param Password:  - str  - Наш пароль
        :param IP_address:  - str  - Наш Айпишник
        :param Headers:  - UM_Headers type/ None - Класс хедера в котором шлем нашу информацию
        :param Auth:  - bool  - Производим или нет авторизацию
        """
        # Переопределяем поля что нам необходимы
        self.Login = Login
        self.Password = Password
        self.IP_address = IP_address
        self.Headers = Headers

        # Если авторизация разрешена - Авторизируемся
        if Auth :
            self.Authorization()

    def Authorization(self):
        """
        Метод Авторизации - для УМ 31 смарт
        :return:
        """
        from JSON_Backend_framework.Devices_USPD.Authorization import Authorization

        Authorization_cookie = Authorization(Login=str(self.Login),
                                             Password=str(self.Password),
                                             ip_address=str(self.IP_address),
                                             headers = self.Headers
                                             )

        # Если авториазия была успешна

        if Authorization_cookie.result_code == 200:
            self.cookie_value = Authorization_cookie.get_cookies()
        else:
            print('Авторизация - не выполнено')
            # Прерываем работу
            # assert Authorization_cookie.result_code == 200, Authorization_cookie.get_result()
            self.cookie_value = None

    def Get_cookie(self):
        """
        Получаем наши Куки
        :return:
        """
        return self.cookie_value

    def Add_cookie(self, cookie_value):
        """
        Абгрейдим наши куки
        :param cookie_value:
        :return:
        """
        self.cookie_value = cookie_value