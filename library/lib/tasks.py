from celery import shared_task
from .models import borrowed_books
from accounts.models import User
from library import settings
import datetime
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta


@shared_task(bind=True,default_retry_delay=300, max_retries=5)
def send_notification(self):
    for x in borrowed_books.objects.all():
        z= User.objects.get(username=x.username)
        r = x.Return - datetime.timedelta(days=1)
        if datetime.datetime.now().date() < r.date():
            print(timezone.localtime(r))
            z.msg1 = True
            z.save()
            subject = 'Welcome to bookworld'
            message = "Hello " + z.first_name + '\n' + 'We are reminding you that your book is due for returning tomorrow\nThank for using bookworld '
            from_email = settings.EMAIL_HOST_USER
            to_list = [z.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
