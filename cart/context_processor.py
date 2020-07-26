from .cart import Cart

def cart_total_amount(request):
	if request.user.is_authenticated:
		cart = Cart(request)
		total_bill = 0.0
		for key,value in request.session['cart'].items():
			total_bill = total_bill + (float(value['price']) * value['quantity'])
		return {'cart_total_amount' : total_bill} 
	else:
		return {'cart_total_amount' : 0} 

def cart_delivery(request):
	if request.user.is_authenticated:
		cta=cart_total_amount(request)
		return {'cart_delivery':(cta['cart_total_amount']//100)*10}
	else:
		return {'cart_delivery':0}

def cart_discount(request):
	if request.user.is_authenticated:
		cta=cart_total_amount(request)
		if cta['cart_total_amount']<=100:
			return {'cart_discount' : 0} 
		else:
			return {'cart_discount':(cta['cart_total_amount']//100)*10}
	else:
		return {'cart_discount':0}

def cart_total(request):
	if request.user.is_authenticated:
		cta=cart_total_amount(request)
		cdt=cart_discount(request)
		cd=cart_delivery(request)
		return {'cart_total':cta['cart_total_amount']+cd['cart_delivery']-cdt['cart_discount']}
	else:
		return {'cart_total':0}