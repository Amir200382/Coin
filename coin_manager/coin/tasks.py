from celery import shared_task
from django.core.mail import send_mail
from .models import CoinWarning
from .views import find_price

@shared_task
def check_and_send_email():
    coins = CoinWarning.objects.all()
    
    for coin in coins:
        coin_data = find_price(coin.name)
        current_price = coin_data['price']
        

        if coin.condition == 1 and current_price > coin.price:  
            if not coin.last_notified_price or coin.last_notified_price < coin.price:
                send_notification_email(coin, current_price)
                coin.last_notified_price = current_price
                coin.save()
                
        elif coin.condition == 0 and current_price < coin.price:  
            if not coin.last_notified_price or coin.last_notified_price > coin.price:
                send_notification_email(coin, current_price)
                coin.last_notified_price = current_price
                coin.save()

def send_notification_email(coin, current_price):
    subject = f"Price Alert for {coin.name}"
    message = f"The price of {coin.name} has met your condition. Current price: {current_price}"
    send_mail(
        subject,
        message,
        'arshiamotaghian@yahoo.com',  
        [coin.email],  
        fail_silently=False,
    )
