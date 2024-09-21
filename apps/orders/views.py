from django.shortcuts import redirect

from apps.books.permissions import new_order_permission
from apps.orders.forms import OrderForm

from django.contrib.auth.decorators import login_required

import telegram

bot = telegram.Bot(token='7474507430:AAGieLlGNHpjvUbluwPpWGWjyP1uPFO2hCY')


@new_order_permission()
def new_order(request, pk):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            bot.sendMessage(733187721, f'Yangi zakaz {form.cleaned_data.get('phone_number')}')
        else:
            print(form.errors)
    else:
        print('get request keldi')
    return redirect('home')
