from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
#, Variation
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse


#@login_required(login_url='login')
#def cart(request):
 #   return render(request, 'store/cart.html')

def _cartid(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_to_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id) #get the product

    try:
            cart = Cart.objects.get(cart_id=_cartid(request)) # get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id = _cartid(request)
            )
    cart.save()

    try:
            cart_item = CartItem.objects.get(product=product, cart=cart)

            cart_item.quantity += 1
            cart_item.save()
    except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
            )
            cart_item.save()
    #return HttpResponse(cart_item.quantity)
    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cartid(request)) # get the cart using the cart_id present in the session
    product = get_object_or_404(Product, id=product_id) #get the product
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else :
        cart_item.delete()
    return redirect('cart')


def remove_cartitem(request, product_id):
    cart = Cart.objects.get(cart_id=_cartid(request)) # get the cart using the cart_id present in the session
    product = get_object_or_404(Product, id=product_id) #get the product
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')

@login_required(login_url='login')
def cart(request, total=0, quantity=0, cart_item=None):
    try:
        cart=Cart.objects.get(cart_id=_cartid(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total +=(cart_item.product.price *cart_item.quantity)
            quantity += cart_item.quantity
        tax = (3 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass
    context = {
        'total' : total,
        'quantity' : quantity,

        'cart_items' : cart_items,
        'tax' : tax,
        'grand_total' : grand_total,
    }

    return render(request, 'store/cart.html', context)


@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        #if request.user.is_authenticated:
            #cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        #else:
        cart = Cart.objects.get(cart_id=_cartid(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass #just ignore

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax'       : tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/checkout.html', context)
