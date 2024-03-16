from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from datetime import datetime
from .models import Product


@shared_task
def send_new_product_notification():
    today = datetime.now().date()

    new_products = Product.objects.filter(created_at__date=today)

    users = User.objects.all()

    for user in users:
        mavzu = 'Yangi mahsulot haqida bildirishnoma'
        message = f"Salom {user.username},\n\nBugun saytga yangi product qo'shilsin\n\nİyi günler!"
        from_email = 'jahonsaitqulov@gmail.com'
        to_email = [user.email]

        send_mail(mavzu, message, from_email, to_email)
