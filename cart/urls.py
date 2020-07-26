from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:id>/',views.add,name='add'),
    path('clear/<int:id>/',views.clear,name='clear'),
    path('increment/<int:id>/',views.increment,name='increment'),
    path('decrement/<int:id>/',views.decrement,name='decrement'),
    path('cart_clear/',views.cart_clear,name='cart_clear'),
    path('detail/',views.detail,name='detail'),
    path('checkout/',views.checkout,name='checkout'),
]

