from django.shortcuts import render
from store.models import Product
#, ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    #.order_by('created_date')

    # Get the reviews
    #reviews = None
    #for product in products:
        #reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        #'reviews': reviews,
    }
    return render(request, 'home.html', context)

#@app.route('/create-checkout-session', methods=['POST'])
#def create_checkout_session():
#    try:
#        checkout_session = stripe.checkout.Session.create(
#            line_items=[
#                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
#                    'price': '{{PRICE_ID}}',
#                    'quantity': 1,
#                },
#            ],
#            mode='payment',
#            success_url=YOUR_DOMAIN + '/success.html',
#            cancel_url=YOUR_DOMAIN + '/cancel.html',
#        )
#    except Exception as e:
#        return str(e)

#    return redirect(checkout_session.url, code=303)
