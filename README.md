# CaptchaBot  

Telegram-bot (python, [aiogram](https://aiogram.dev/))

Captcha for incoming telegram chats users.

### Launching in Docker

Create and start container:

```bash
$ export BOT_TOKEN=<BOT_TOKEN>
$ export CHAT_ID_1=<CHAT_ID_1>
$ export CHAT_ID_2=<CHAT_ID_2>
$ export CHAT_ID_3=<CHAT_ID_3>
$ export CHAT_ID_4=<CHAT_ID_4>
$ docker-compose up -d
```

Stop lifted containers:

```bash
$ docker-compose stop
```

Start stopped containers:

```bash
$ docker-compose start
```

Stop and delete containers and network:

```bash
$ docker-compose down
```

Remove image:

```bash
$ docker rmi captcha_bot
```

Clear logs:

```bash
$ sudo rm -rf logs/*
```

Execute a command in a running container:

```bash
$ docker exec -it CaptchaBot bash
```
