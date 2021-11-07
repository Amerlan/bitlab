from bitalb.celery import celery_app
from datetime import datetime
from time import sleep

@celery_app.task
def send_email(email, message):
    # Замеряем время до начала задачи
    start = datetime.now()
    print(f'Пытаемся отправить сообщение пользователю \n{email} \nс текстом: \n{message}')
    # иммитация реального отправления сообщения
    sleep(10)
    # Замеряем время после "отправки" сообщения
    end = datetime.now()
    total_email_time = end - start
    print(f'Сообщение доставлено успешно за {total_email_time}')