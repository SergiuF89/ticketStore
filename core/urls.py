from django.conf.urls import url
from django.urls import path

from items.views import search
from .views import (
    ItemDetailView,
    CheckoutView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
)
from posts.views import HomeView, CategoryRockView, CategoryHouseView, CategoryHipHopView
from users.views import ProfileView, UserProfileView



app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='all-categories'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('rock/', CategoryRockView.as_view(), name='rock-category'),
    path('house/', CategoryHouseView.as_view(), name='house-category'),
    path('hip_hop/', CategoryHipHopView.as_view(), name='hip-hop-category'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile-view'),
    path('profile/update/<int:pk>', ProfileView.as_view(), name='profile-update'),
    url(r'^shop/$', search, name = 'search'),
]
