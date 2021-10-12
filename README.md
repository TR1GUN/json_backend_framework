# JSON-Backend-Tests

Здесь расположим тесты для JSON-Backend



-----------
### ChargeStationTable

Таблица зарядных станций

- `read_settings()` - Читаем данные - GET
- `write_settings()` - Добавляем на запись данные - POST    
    Переменные:
   - `data` - `dict` , `None` - Данные в Формате JSON. Если None - то используем добавленные данные
- `rewrite_settings()` - Перезаписываем данные - PUT      
    Переменные:
   - `data` - `dict` , `None` - Данные в Формате JSON. Если None - то используем добавленные данные
- `delete_settings()` - Удаляем данные - DELETE     
   - `data`: Данные в Формате JSON - Если None - то используем добавленные данные - Если их нет, то никакой idx не будет задан
    
Пример JSON который можно отправлять на запись\перезапись
```json
{
  settings: {
                'addr': IP_address,
                'id': Device_idx,
                'mqttId': ID_MQTT,
                'port': IP_port,
                'type': type
            }
}
```
Пример JSON который можно отправлять на удаление
```json
{
  settings : {
                'id': []
             }
}
```

Добавление своих элементов массива по-одному     
В классе есть поле `Data_Settings` через который можно добавлять свои настройки для использования в основном классе.   
Это поле является объектом класса со своими методами.   
Методы Класса:
- `add_settings()` - Добавление настроек для записи :   
  - `Device_idx` - int - ID станции - поле  id
  - `IP_address` - str - IP адрес станции  - поле  addr
  - `IP_port` - int - IP порт станции  - поле  port
  - `ID_MQTT` - int - ID MQTT брокера - поле  mqttId
  - `type` -  str - Тип станции - По умолчанию заполняется значением ZSE-500T (Единственное поддерживаемое значение) - поле type
  

- `remove_settings()` -  Удаление добавленной записи settings для записи по ID    
  - `idx` - list or int
  
- `get_settings()` - Получаем добавленные settings

- `add_ids()` - Добавляем Device_id для запроса данных или удаления
  - `ids` - Сам Id

- `remove_ids()` - Удаление добавленной записи ids для получения/удаления записей
  - `param ids` - list or int
  
- `get_ids` - Получаем добавленные settings

-----------
### ChargeStationArchData

Таблица данных зарядных станций.
Запрашивает данные.
- `read_settings_StationParams()` - считываем данные: Состояние зарядных станций — таблица StationParams
  - `ids` - `int/list/None` - ID станций — Если None, то не формируется поле ids
  - `time_end` - `int/None` - Время конца считывания. Если None - и задано время старта — то ставиться текущая дата + 1000.  Если время старта не задано, то поле time не формируется
  - `time_start` - `int/None` - Время старта считывания. Если None - и задано время конца — то ставиться 0. Если время конца не задано, то поле time не формируется

- `read_settings_chargeProcessParams()` - считываем данные:Состояние процесса заряда — таблица chargeProcessParams
  - `ids` - `int/list/None` - ID станций — Если None, то не формируется поле ids
  - `time_end` - `int/None` - Время конца считывания. Если None - и задано время старта — то ставиться текущая дата + 1000.  Если время старта не задано, то поле time не формируется
  - `time_start` - `int/None` - Время старта считывания. Если None - и задано время конца — то ставиться 0. Если время конца не задано, то поле time не формируется

- `read_settings_chargeSessionParams()` - считываем данные:История зарядных сессий — таблица chargeSessionParams
  - `ids` - `int/list/None` - ID станций — Если None, то не формируется поле ids
  - `time_end` - `int/None` - Время конца считывания. Если None - и задано время старта — то ставиться текущая дата + 1000.  Если время старта не задано, то поле time не формируется
  - `time_start` - `int/None` - Время старта считывания. Если None - и задано время конца — то ставиться 0. Если время конца не задано, то поле time не формируется

- `read_settings()` - Формирование запроса на чтение данных в нужной таблице
  - `measure` - `str` - Обязательное значение — имя таблицы, что читаем. 
    - Допустимые значения: 
      - `chargeSessionParams` 
      - `chargeProcessParams` 
      - `stationParams` 
      - `chargeStations`
    
  - `ids` - `int/list/None` - ID станций — Если None, то не формируется поле ids
  - `time_end` - `int/None` - Время конца считывания. Если None - и задано время старта — то ставиться текущая дата + 1000.  Если время старта не задано, то поле time не формируется
  - `time_start` - `int/None` - Время старта считывания. Если None - и задано время конца — то ставиться 0. Если время конца не задано, то поле time не формируется
  
-----------
###MeterDeviceTable    

Таблица приборов учета

- `read_settings()` - Читаем данные - GET
- `write_settings()` - Добавляем на запись данные - POST    
    Переменные:
   - `data` - `dict` , `None` - Данные в Формате JSON. Если None - то используем добавленные данные
- `rewrite_settings()` - Перезаписываем данные - PUT      
    Переменные:
   - `data` - `dict` , `None` - Данные в Формате JSON. Если None - то используем добавленные данные
- `delete_settings()` - Удаляем данные - DELETE     
   - `data`: Данные в Формате JSON - Если None - то используем добавленные данные - Если их нет, то никакой idx не будет задан
    
Пример JSON который можно отправлять на запись\перезапись
```json
    {
        "Meters": [
            {
                "id": 1,
                "pId": 0,
                "typeName": "Mercury23x",
                "addr": "72",
                "passRd": "010101010101",
                "passWr": "020202020202",
                "ifaceName": "Iface1",
                "ifaceCfg": "9600,8n1",
                "rtuObjType": 3,
                "rtuObjNum": 2,
                "rtuFider": 1
            }
        ]
    }
```
Пример JSON который можно отправлять на удаление
```json
{
  Meters : {
                'id': []
             }
}
```

Добавление своих элементов массива по-одному     
В классе есть поле `Data_Settings` через который можно добавлять свои настройки для использования в основном классе.   
Это поле является объектом класса со своими методами.   
Методы Класса:
- `add_settings()` - Добавление настроек для записи :   
   - `MeterId` - `int - ID Счетчика. Используется для взаимодействия со счетчика в дальнейшем.
   - `typeName_Meter` - `str - Имя типа счетчика. Можно получить все типы поддержанных счетчиков через метод get_permissible_meters
   - `Interface` - `str - Имя типа подключения по Интерфейсу. Можно получить все типы поддержанных Интерфейсов через метод get_permissible_interface
   - `address` - `str` - Адрес счетчика
   - `password_to_read` - `str - Пароль доступа 1 уровня - На чтение
   - `password_to_write` - `str - Пароль доступа 2 уровня - На запись
   - `ParentId` - `int` - Id Родительского устройства. Если его нет, то ставиться 0. Значение по умолчанию - 0
   - `ifaceConfig` - `str` - Настройки интерфейса . Значение по умолчанию - '9600,8n1
   - `rtuObjType` - `int` - Тип объекта RTU . Значение по умолчанию - 0
   - `rtuObjNum` - `int` - Номер объекта RTU . Значение по умолчанию - 0
   - `rtuFider` - `int` - Фидер объекта RTU . Значение по умолчанию - 0

Поддерживаемые значения для интерфейсов :   
    - Интерфейс 1 - `Iface1`   
    - Интерфейс 2 - `Iface2`   
    - Интерфейс 3 - `Iface3`   
    - Интерфейс 4 - `Iface4`   
    - Ethernet - `Ethernet`   
    - Интерфейс концентратора - `Hub`  


Поддерживаемые значения для Счетчиков :   
    - Меркурий200 - `Mercury200`   
    - Меркурий203 - `Mercury203`  
    - Меркурий206 - `Mercury206`   
    - Меркурий23x - `Mercury23x`  
    - Меркурий234 СПОДЭС - `SPODES`   
    - СЕ102 - `SE102`   
    - СЕ102М - `SE102M`   
    - СЕ301 - `SE301`   
    - СЕ303 - `SE303`    
    - СЭБ2А - `SEB2a`   
    - СЭТ4ТМ - `SETxTM`   
    - ПСЧхТМ - `PSCHxTM`   
    - Альфа1140 - `A1140`   
    - ТОПАЗ - `TOPAZ`   
    - НЕВА1xx - `NEVA1xx`   
    - НЕВА3xx - `NEVA3xx`    
    - МИЛУР IC - `MILUR IC`   
    - Милур10x - `MILUR10x`    
    - Милур30x - `MILUR30x`    
    - СОЭ55/215 - `SOE55_215`    
    - СОЭ55/217 - `SOE55_217`     
    - СОЭ55/415 - `SOE55_415`    
    - СТЭ561 - `STE561`    
    - ИНТЕГРА10х - `INTEGRA10x`    
    - УМТВ10 - `UMTV10`    
    - Пульсар - `Pulsar`     
    - ST410 - `ST410`   


- `remove_settings()` -  Удаление добавленной записи settings для записи по ID    
  - `idx` - list or int
  
- `get_settings()` - Получаем добавленные settings

- `add_ids()` - Добавляем Device_id для запроса данных или удаления
  - `ids` - Сам Id

- `remove_ids()` - Удаление добавленной записи ids для получения/удаления записей
  - `param ids` - list or int
  
- `get_ids` - Получаем добавленные settings

-  `get_permissible_meters()` - Получаем размещенные счетчики

- `get_permissible_interface()` Получаем добавленные ids
-----------

























-----------
#Примеры JSON :

-----------
## :floppy_disk: Для таблицы chargeProcessParams

### POST
Запрос
```json
{"method": "post", "data": [{"table": "chargeProcessParams", "values": [
{"chargeLevel" : 2,"sessionId" : 2,"stationId" : 2,"stationTableId" : 2,"time" : 2}]}]}
```
Варианты ответа:
```json
 {"res": 0.0}
```
```json
{"error": "Income message error", "res": 74.0}
```
### GET
Запрос
```json
{"method": "get", "data": [{"table": "chargeProcessParams", "ids":[2], "time":[{"start":0, "end":9}] }]}
```
```json
{"method": "get", "data": [{"table": "chargeProcessParams", "ids": []}]}
```
```json
{"method": "get", "data": [{"table": "chargeProcessParams"}]}
```

Варианты ответа:
```json
{"data" :[{"table" : "chargeProcessParams",  "values" : [ {
 "chargeLevel" : 2, "sessionId" : 2, "stationId" : 2, "stationTableId" : 2, "time" : 2} ] } ], "res" : 0.0}
```
### PUT
Запрос
```json
{"method": "put", "data": [{"table": "chargeProcessParams", "values": [
{"chargeLevel" : 2,"sessionId" : 2,"stationId" : 2,"stationTableId" : 2,"time" : 2}]}]}

```

Варианты ответа:
```json
 {"res": 0.0}
```
```json
{"error": "Income message error", "res": 74.0}
```
### DELETE
Запрос
```json
{"method": "delete", "data": [{"table": "chargeProcessParams","ids":[1]}]}
```
```json
{"method": "delete", "data": [{"table": "chargeProcessParams"}]}
```

Варианты ответа:
```json
 {"res": 0.0}
```
```json
{"error": "Income message error", "res": 74.0}
```
-----------