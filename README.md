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

###MeterArchData    

Основной класс работы с Архивными данными 

Методы Класса:
- `read_data_to_measure()` - прочитать архивные данные вводимого типа данных:

   - `measure` - `str` - Обязательное значение - типа данных что читаем. Допустимые значения :

   - `ids` - `int/list/None` - Meter ID  - Если None, то не формируется поле ids

   - `time_end` - `int/None` - Время конца считывания. Если None - и задано время старта - то ставиться текущая дата  + 1000.  Если время старта не задано то поле time не формируется

   - `time_start`- `int/None` - Время старта считывания. Если None - и задано время конца - то ставиться 0. Если время конца не задано то поле time не формируется

   - `tags` - `None/list/str` - Тэги что запрашиваем - Если None, то тэг не ставиться, если строка - то тэг что указан в строке, если список , то список тэгов что указан в массиве.

- `get_measures()` - получение словаря всех типов данных measure в формате "measure_name":"расшифровка"

Так же можно считать нужный тип данных, обратившись по его одноименному методу в соответствующем поле класса.   

Пример : 
```python
    Elconfig = MeterArchData().Electric.ElConfig()
```
- `read()` - Отправить свой JSON запрос

   - `data` - `dict` - словарь запроса
    
Пример : 
```json
    {           "ids": [],
            "tags": [
                "A+0","A+1","A+2","A+3","A+4","A-0","A-1","A-2","A-3","A-4",
                "R+0","R+1","R+2","R+3","R+4","R-0","R-1","R-2","R-3","R-4"],
            "measures": ["ElMomentEnergy"]}
```
Поля класса:
- `Journal` - Типы данных журналов
- `Pulse` - Типы данных импульсных концентраторов
- `Digital` - Типы данных дискретных концентраторов
- `Electric` - Типы данных Электросчетчиков

При вызове функций используются все те же переменные указанные выше кроме переменной `measure`.    
При вызове функций журналов так же отсутствует переменная `tags`


Поддерживаемые типы данных (если тип данных не верен, то возвращается _None_ ):     
        
- `ElConfig` - конфигурация электросчетчика
- `PlsConfig` - конфигурация модуля дискретных вводов/выводов
- `DigConfig` - конфигурация концентратора импульсных счетчиков
- `ElMomentEnergy` - мгновенные показания энергии электросчетчика
- `ElDayEnergy` - показания электросчетчика на начало суток
- `ElMonthEnergy` - показания электросчетчика на начало месяца
- `ElDayConsEnergy` - потребление электросчетчика за сутки
- `ElMonthConsEnergy` - потребление электросчетчика за месяц
- `ElMomentQuality` - мгновенные ПКЭ
- `ElArr1ConsPower` - профили мощности первого массива профилей мощности электросчетчика
- `PlsMomentPulse` - мгновенные показания энергии концентратора импульсных счетчиков
- `PlsDayPulse` - показания концентратора импульсных счетчиков на начало суток
- `PlsMonthPulse` - показания концентратора импульсных счетчиков на начало месяца
- `PlsHourPulse` - показания на начало часа концентратора импульсных счетчиков
- `DigMomentState` - мгновенные показания модуля дискретных вводов/выводов
- `DigJournalState'` - архив изменения состояний модуля дискретных вводов/выводов
- `ElJrnlPwr` - журнал управление питанием
- `ElJrnlTimeCorr` - журнал коррекция времени электросчетчика
- `ElJrnlReset` - журнал сброс показаний
- `ElJrnlC1Init` - журнал инициализация первого массива профилей
- `ElJrnlC2Init` - журнал инициализация второго массива профилей
- `ElJrnlTrfCorr` - журнал коррекция тарификатора
- `ElJrnlOpen` - журнал открытие крышки
- `ElJrnlUnAyth` - журнал неавторизованный доступ
- `ElJrnlPwrA` - журнал управление фазой А
- `ElJrnlPwrB` - журнал управление фазой В
- `ElJrnlPwrC` - журнал управление фазой С
- `ElJrnlProg` - журнал программирование
- `ElJrnlRelay` - журнал управление реле
- `ElJrnlLimESumm` - журнал лимит суммарной энергии
- `ElJrnlLimETrf` - журнал потарифиный лимит энергии
- `ElJrnlLimETrf1` - журнал лимит энергии тарифа 1
- `ElJrnlLimETrf2` - журнал лимит энергии тарифа 2
- `ElJrnlLimETrf3` - журнал лимит энергии тарифа 3
- `ElJrnlLimETrf4` - журнал лимит энергии тарифа 4
- `ElJrnlLimUAMax` - журнал ограничение максимального напряжения фазы А
- `ElJrnlLimUAMin` - журнал ограничение минимального напряжения фазы А
- `ElJrnlLimUBMax` - журнал ограничение максимального напряжения фазы В
- `ElJrnlLimUBMin` - журнал ограничение минимального напряжения фазы В
- `ElJrnlLimUCMax` - журнал ограничение максимального напряжения фазы С
- `ElJrnlLimUCMin` - журнал ограничение минимального напряжения фазы С
- `ElJrnlLimUABMax` - журнал ограничение максимального расхождения напряжения фаз А и В
- `ElJrnlLimUABMin` - журнал ограничение минимального расхождения напряжения фаз А и В
- `ElJrnlLimUBCMax` - журнал ограничение максимального расхождения напряжения фаз В и С
- `ElJrnlLimUBCMin` - журнал ограничение минимального расхождения напряжения фаз В и С
- `ElJrnlLimUCAMax` - журнал ограничение максимального расхождения напряжения фаз С и А
- `ElJrnlLimUCAMin` - журнал ограничение минимального расхождения напряжения фаз С и А
- `ElJrnlLimIAMax` - журнал ограничение максимального тока фазы А
- `ElJrnlLimIBMax` - журнал ограничение максимального тока фазы В
- `ElJrnlLimICMax` - журнал ограничение максимального тока фазы С
- `ElJrnlLimFreqMax` - журнал ограничение максимальной частоты сети
- `ElJrnlLimFreqMin` - журнал ограничение минимальной частоты сети
- `ElJrnlLimPwr` - журнал ограничение мощности
- `ElJrnlLimPwrPP` - журнал ограничение прямой активной мощности
- `ElJrnlLimPwrPM` - журнал ограничение прямой реактивной мощности
- `ElJrnlLimPwrQP` - журнал ограничение обратной активной мощности
- `ElJrnlLimPwrQM` - журнал ограничение обратной реактивной мощности
- `ElJrnlReverce` - журнал реверс
- `PlsJrnlTimeCorr` - журнал коррекция времени концентратора импульсных счетчиков

-----------
ДЕЙСТВИЯ 


-----------
### DeviceRestart

Перезагрузка устройства

DeviceRestart

Методы Класса:

- `Restart()` - Перезагружает устройство





-----------

###SetTimeSetting    

Основной класс работы с Установкой системного времени на устрйостве 

По умолчанию использует текущее время компьютера.
Значения можно переопределить с помощью методов класса


Методы Класса:

- `Setup_Time_Set()` - Отправляем переменную времени.   
  Значения по умолчанию — текущее время. Если время не изменялось, то используются значения по Умолчанию.

- `add_Year()` - Установка пользовательского года в переменную времени
   - `Year` - `str/int` - Год - Формат - 2021
    
- `add_Month()` - Установка пользовательского Месяца в переменную времени
   - `Month` - `str/int` - Месяц - Формат - 02

- `add_Day()` - Установка пользовательского Дня в переменную времени
   - `Day` - `str/int` - День - Формат - 01

- `add_Hour()` - Установка пользовательского Часа в переменную времени
   - `Hour` - `str/int` - ЧАС - Формат - 24 часа - 18 или 01

- `add_Minute()` - Установка пользовательской Минуты в переменную времени
   - `Minute` - `str/int` - Минуты - Формат - 09

- `add_Second()` - Установка пользовательской Секунды в переменную времени
   - `data` - `str/int` - Секунды - Формат - 7 - '07'

- `add_Time_Zone()` - Установка пользовательского Часового пояса в переменную времени
   - `Time_Zone` - `str` - Часовой пояс - Формат +03:00


- `Setup_JSON()` - Отправить пользовательский JSON вместо переменной времени.  

   - `data` - `dict` - Обязательное значение — Пользовательский JSON в формате Backend.
           Пример : 
        ```json
        {"time": "2007-10-15T01:33:25+10:00"} 
        ``` 
Пример Запуска : 
```python
    SetTime = SetTimeSetting().Setup_JSON(data={"time": "2007-10-15T01:33:25+10:00"})
```
или 
```python
    SetTime = SetTimeSetting()
    SetTime.add_Year(1960)
    SetTime.add_Month(10)
    SetTime.add_Day(15)
    SetTime.add_Hour(1)
    SetTime.add_Minute(33)
    SetTime.add_Second(25)
    SetTime.add_Time_Zone("+10:00")
    result  = SetTime.Setup_Time_Set()
```
-----------

-----------
### EthernetSettings

Настройки Ethernet

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
{"Settings": [
            {"iface": "eth0", 
              "dhcp": false, 
              "ip":"192.168.0.1", 
              "netmask": "255.255.255.1", 
              "gw": "", 
              "dns1": "", 
              "dns2": ""},
            {"iface": "eth1", 
              "dhcp": true, 
              "ip":"", 
              "netmask": "", 
              "gw": "", 
              "dns1": "", 
              "dns2": ""}
              ]}

```
Пример JSON который можно отправлять на удаление
```json
{"Settings": [
            {"iface": "eth0", 
              "dhcp": false, 
              "ip":"", 
              "netmask": "", 
              "gw": "", 
              "dns1": "", 
              "dns2": ""},
            {"iface": "eth1", 
              "dhcp": true, 
              "ip":"", 
              "netmask": "", 
              "gw": "", 
              "dns1": "", 
              "dns2": ""}
              ]}
```

Добавление своих элементов массива по-одному     
В классе есть поле `Ethernet_Settings` через который можно добавлять свои настройки для использования в основном классе.   
Это поле является объектом класса со своими методами.   
Методы Класса:   
Для интерфейса Ethernet 1 :
- `added_Eth_0()` - Добавление настроек для записи настроек интерфейса Ethernet 1:     
  - `dhcp` - `bool` - Настройки DHCP
  - `ip` - `str` - Настройки IP адреса
  - `netmask` - `str` - Маска подсети
  - `gateway` - `str` - Шлюз
  - `dns1` - `str` - DNS Первичный Сервер
  -  `dns2` - `str` - DNS Вторичный Сервер

- `remove_Eth_0()` -  Удаление настроек интерфейса Ethernet 1, что ввели
  
- `settings_Eth_0()` - Получить настройки Ethernet 1


Для интерфейса Ethernet 2 :
- `added_Eth_1()` - Добавление настроек для записи настроек интерфейса Ethernet 2:     
  - `dhcp` - `bool` - Настройки DHCP
  - `ip` - `str` - Настройки IP адреса
  - `netmask` - `str` - Маска подсети
  - `gateway` - `str` - Шлюз
  - `dns1` - `str` - DNS Первичный Сервер
  -  `dns2` - `str` - DNS Вторичный Сервер

- `remove_Eth_1()` -  Удаление настроек интерфейса Ethernet 2, что ввели
  
- `settings_Eth_1()` - Получить настройки Ethernet 2
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