# -------------------------------------------------------------------------------------------------------------
#                                              Шаблон Формирования JSON
#                                                   Управление реле
# -------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------

class TemplateFormJSON_Relay:
    """
    Шаблон для JSON - Управление реле
    """
    # Готовый запрос
    _Setting_Relay = None

    # ID счетчика
    _MeterId = None
    # ID реле
    _RelayId = None
    # Положение реле
    _RelayState = None

    # Добавляем
    def add_Value(self, MeterIdx: int, RelayId: int, RelayState: [int, bool]):
        """
        Установка положения реле на счетчике по его MeterIdx
        :param MeterIdx: ID счетчика
        :param RelayId: ID реле
        :param RelayState: Положение реле - вкл - 1б выкл - 0
        :return:
        """
        # Продолжаем только в том случае если реле заданно
        if MeterIdx:
            try:
                self._MeterId = int(MeterIdx)
            except Exception as e:
                error = "Error value Meter Id: " + str(MeterIdx) + ".\n Error Exception : " + str(e)
                print(error)
                self._MeterId = 0

            # Далее задаем Реле
            try:
                self._RelayId = int(RelayId)
            except Exception as e:
                error = "Error value RelayId : " + str(RelayId) + ".\n Error Exception : " + str(e)
                print(error)
                self._RelayId = 0

            # Задаем положение реле
            try:
                self._RelayState = int(RelayState)
            except Exception as e:
                error = "Error value RelayState: " + str(RelayState) + ".\n Error Exception : " + str(e)
                print(error)
                self._RelayState = 0

    # Удаляем
    def remove_Value(self):
        """
        Удаление записанного положения Реле
        """
        # ID счетчика
        self._MeterId = None
        # ID реле
        self._RelayId = None
        # Положение реле
        self._RelayState = None

    def get_JSON(self):
        """
        Получаем наши данные что составили
        """
        self._Setting_Relay = \
            {
                "id": int(self._MeterId),
                "relayId": int(self._RelayId),
                "relayState": int(self._RelayState),
            }

        return self._Setting_Relay
