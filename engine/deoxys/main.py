from celery import Celery
from celery.schedules import crontab
from celery.decorators import periodic_task
from datetime import timedelta

app = Celery()

code1 = "from time import sleep\n\nwhile 1:\n    print \"I am here with 7\"\n    sleep(7)\n"
code2 = "from time import sleep\n\nwhile True:\n    print \"I am here with 3\"\n    sleep(3)\n"

@app.task
exec(code1)

@app.task
exec(code2)
