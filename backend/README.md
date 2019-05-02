# Спецификация 

В данном релиз бекэнд содержит в себе следующий функционал:

* регистрация и авторизация пользователя;
* выход пользователя из системы;
* шифрование пароля;
* сессия пользователя;
* создание чата;
* передача сообщений между пользователями.

## 1. Регистрация и авторизация пользователя

При регистрации к пользователю предъявляются следующие требования:
* длина логина не больше 20 символов;
* логин должен быть уникальным.

**(?)** А если больше 20 симоволов?

### Регистрация

Для регистрации пользователя, клиент должен отправить следующий json-запрос

```
  "Type": "registration",
  "Login": "user",
  "Password": "password"
```
Сервер ответит
```
  "Type": "registration",                                            
  "Status": "success"
```

### Зарегистрированный пользователь

Если пользователь попробует зарегистрироваться под уже имеющимся в базе логином, то сервер ответит так
```
  "Type": "registration",
  "Status": "user exist"
```



***FAQ***

*Нужно ли авторизовываться после регистрации?* 
Нет, не нужно. Однако стоит проверить этот факт.

### Авторизация

Для авторизации пользователя клиент должен отправить следующий json-запрос

```
  "Type": "login",
  "Login": "user",
  "Password": "password"
```
Сервер ответит
```
  "Type": "login",
  "Status": "success"
```

### Неверный пароль или несуществующий пользователь
Если пользователь введет неверный пароль или логин не существует в базе, сервер ответит ему так
```
  "Type": "login",
  "Status": "error"
```

## 2. Выход пользователя из системы
Чтобы совершить выход из системы, клиент должен отправить на сервер
```
  "Type": "logout",                                                   
  "Login": "user"
```
Сервер ответит
```
  "Type": "logout", 
  "Status": "success"
```
**(?)** Однако стоит задуматься, нужно ли вообще серверу отправлять ответ?

### Выход не авторизованного пользователя
Если пользователь не имеющий логина и не авторизованный в системе отправит запрос на выход, сервер ответит так
```
  "Type": "logout", 
  "Status": "error"
```
## 3. Шифрование паролей
Пользователь может быть спокоен, все пароли хранятся в sha-512 + salt(sha256 + random) 

## 4. Сессия пользователя
Сессия пользователя автоматически создаётся при входе или регистрации пользователя. Сессия хранит идентификатор пользователя и время входа в систему.

## 5. Чат
При создании чата перед пользователем предъявляются следующие требования:
* длина имени чата не должна превышать 32 символов;
* пользователь должен быть авторизован в системе.

Для создания чата клиент должен отправить json-запрос с следущим содержанием
```
  "Type": "chat",                                                     
  "User": "user",
  "Command": "create"                                                     
  "Chat": "general"
```
При успешном создании чата сервер ответит
```
  "Type": "chat", 
  "Status": "success"
```
Если неавторизованный пользователь попробует создать чат, сервер ответит ему так
```
  "Type": "chat", 
  "Status": "chat exist"
```
**(?)** А почему chat exist?
**(?)** До конца не реализована функция, тк нет редиректа. 

Для получения всех чатов пользователя нужно отправить
```
  "Type": "chat",
  "Command": "get"
```
**(?)** А если не авторизованный пользователь?

## 6. Сообщения
Перед отправкой сообщения пользователь должен быть:
* авторизован;
* чат должен существовать.

Для отправки сообщения в чат клиент должен отправить сообщение 
```
  "Type": "message",                                                  
  "User": "user",                                                     
  "Chat": "general",                                                  
  "Text": "Hey, there is somebody?"
```
На что сервер ответит, почти точно таким же сообщеним каждому подключенному пользователю
```
  "Type": "message",
  "Status": "success",
  "User": "user",                                                     
  "Chat": "general",                                                  
  "Text": "Hey, there is somebody?"
```
**Почему так?** Это происходит потому что, все общение идет через сервер. А значит мы должны отправлять только те сообщения которые гарантированно дошли до сервера и сохранены в базе.

**(?)** Сообщение придет во все комнаты, бродкаст. TODO: Сообщения внутри чата.
**(?)** Обработать сообщение "Status": "error", например когда база недоступна или память кончилась, или сервер упал.

Если авторизованный пользователь попробует отправить в несуществующий чат сервер ему ответит
```
  "Type": "chat", 
  "Status": "chat not exist"
```

Так будет с каждым, кто дочитает спецификацию до конца.