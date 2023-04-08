from django.shortcuts import render, redirect
from django.http import HttpResponse
#, JsonResponse
from carts.models import CartItem
from .forms import OrderForm
import datetime
from .models import Order, Payment, OrderProduct
import json
from store.models import Product
#from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import stripe

def payments(request):
    return render(request, 'orders/payments.html')

def place_order(request):
    return redirect('order_complete')
            #return render(request, 'orders/payments.html', context)

    #else:
        #return redirect('place_order')


    #return render(request, 'orders/payments.html', context)

#stripe.api_key = settings.STRIPE_SECRET_KEY
#@app.route('/create-checkout-session', methods=['POST'])


def order_complete(request):
        return render(request, 'orders/order_complete.html')
