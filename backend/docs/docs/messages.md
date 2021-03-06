# Сообщения

Перед отправкой сообщения пользователь должен быть:

* авторизован;
* чат должен существовать.

Прежде чем отправить сообщение пользователь должен выбрать чат.

```json
{
	"Type": "chat",
	"Chat": "general",
	"Command": "choice"
}
```
Только после, пользователь может приступать к отправке сообщения.

## Отправка сообщения

Для отправки сообщения в чат клиент должен отправить сообщение

```json
{
	"Type": "chat",
	"Command": "message",
	"Text": "Hey, there is somebody?"
}
```

На что сервер ответит, точно таким же сообщением каждому подключенному пользователю

```json
{
	"Type": "chat",
	"Command": "message",
	"Message": {
		"id" : "338",
		"user": "user",
		"text": "Hey, there is somebody?",
	}
}
```

**Почему так?** Это происходит потому что, все общение идет через сервер. А значит мы должны отправлять только те сообщения которые гарантированно дошли до сервера и сохранены в базе.

## Ошибки при отправке сообщения

Если пользователь попрообует отправить сообщение не авторизованныем или не выбрав чат, сервер ответит

```json

{
	"Type": "chat",
	"Command": "message",
	"Status": "error in chat or user"
}
```

**(?)** Обработать сообщение "Status": "error", например когда база недоступна или память кончилась, или сервер упал.

Если авторизованный пользователь попробует отправить в несуществующий чат сервер ему ответит

```json
{
	"Type": "chat",
	"Status": "error"
}
```

## Отправка изображения

Для отправки изображения клиент должен перевести изображение в base64

```json
{
	"Type": "chat",
	"Command":"message",
	"Image": "WW91IGEgcGlkb3IK"
}
```
В случае успеха сервер ответит

```json
{
	"Type": "chat",
	"Command": "message",
	"Message": {
		"id" : "339",
		"user": "user",
		"image": "/images/{chat}/{md5}.{extentsion}",
	}
}
```

### Отправка изображения с сообщением

Все так же как и с отправкой изображения, для отправки изображения клиент должен перевести изображение в base64

```json
{
	"Type": "chat",
	"Command":"message",
	"Image": "WW91IGEgcGlkb3IK",
	"Text": "LOL"
}
```
В случае успеха сервер ответит

```json
{
	"Type": "chat",
	"Command": "message",
	"Message": {
		"id": "340",
		"user": "user",
		"image": "/images/{chat}/{md5}.{extentsion}",
		"text": "LOL"
	}
}
```

Если кто-то захочет загрузить, что-то помимо изображения, сервер ответит так

```json
{
	"Type": "chat",
	"Command": "message",
	"Status": "failed to attach image"

}
```
## Ответ на сообщение

Ответ на сообщение мало чем отличается от ответа на сообщение

```json
{
	"Type": "chat",
	"Command": "message",
	"Text": "I not understand this message",
	"Reply": {
    	"id": "359",
     }
}
```

В валидном случае сервер ответит


```json
{
	"Type": "chat",
	"Command": "message",
	"Message": {
		"Text": "I not understand this message",
		"id": "360",
		"Reply": {
	    	"id": "359",
	    	"user": "user", 
	    	"date": "2019-07-19 10:51:16", 
	    	"text": "Test reply message"
	     }
	}
	
}
```

### Ошибочный ответ

В случае не найденного в базе сообщения сервер ответит

```json

{
	"Type": "chat",
	"Command": "message",
	"Status": "message does not exist"
}
```



