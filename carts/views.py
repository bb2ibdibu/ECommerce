# 
# 视图函数是Django框架中用于处理HTTP请求并返回HTTP响应的一种函数。
# 在Django框架中，视图函数是一个Python函数，它接收一个HttpRequest对象作为参数，
# 并返回一个HttpResponse对象。
# 当用户访问网站时，浏览器会向服务器发送HTTP请求，
# 在服务器端，Django会根据URL配置找到对应的视图函数来处理这个请求，并将结果封装成HttpResponse对象返回给浏览器。
# 因此，可以说视图函数是实现Web页面逻辑的核心部分。
# 在编写视图函数时，我们可以通过模板引擎、数据库等方式获取数据并渲染HTML页面或者其他格式的响应内容。

from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (10 * total)/100
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
    return render(request, 'store/cart.html', context)


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id) #get the product
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
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
    return redirect('cart')

def remove_cart(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
   
    return redirect('cart')

def remove_cart_item(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)

    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')