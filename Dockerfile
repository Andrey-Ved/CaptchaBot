FROM python:3.11.2-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ~/CaptchaBot

COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

COPY captcha_bot ./captcha_bot

CMD ["python", "-m", "captcha_bot"]

# -------------------------------
# Build an image from a Dockerfile:
# $ docker build -t captcha_bot .
# -------------------------------
# Create and run a new container from an image:
# $ docker run -d --name CaptchaBot \
#    --env "BOT_TOKEN=<BOT_TOKEN>" \
#    --env "CHAT_ID_1=<CHAT_ID_1>" \
#    --env "CHAT_ID_2=<CHAT_ID_2>" \
#    --env "USERS_DATA_FILE=<USERS_DATA_FILE>" \
#    captcha_bot
# -------------------------------
# Stop running container:
# $ docker stop CaptchaBot
# -------------------------------
# Start stopped container:
# $ docker start CaptchaBot
# -------------------------------
# Remove container:
# $ docker rm CaptchaBot
# -------------------------------
# Remove image:
# $ docker rmi CaptchaBot
# -------------------------------
# Execute a command in a running container:
# $ docker exec -it CaptchaBot bash
