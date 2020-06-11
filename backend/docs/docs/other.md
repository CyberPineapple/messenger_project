# Шифрование паролей
Пользователь может быть спокоен, пароли от акканта хранятся в sha-512 + salt(sha256 + random), пароли от чата хранятся в sha-256 + salt(sha128 + random).


# Сессия пользователя
Сессия пользователя автоматически создаётся при входе или регистрации пользователя. Сессия хранит идентификатор пользователя и время входа в систему и текущий чат.



# Команда для создания базы данных с utf-8 кодировкой

	create database Messenger with encoding='utf-8' LC_CTYPE='en_US.utf8' LC_COLLATE='en_US.utf8' TEMPLATE template0;

# Запусе севера 

	gunicorn -c settings.ini  server:main --worker-class aiohttp.worker.GunicornWebWorker