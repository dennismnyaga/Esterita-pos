from django.urls import path
from . import views



from .views import  MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('products/', views.all_products, name='products'),
    path('prods/', views.all_prods, name='prod'),
    path('employees/', views.all_emplyees, name='employees'),
    path('cart/', views.all_cart, name='cart'),
    path('colors/', views.all_colors, name='colors'),
    path('materials/', views.all_material, name='material'),
    path('prosize/', views.all_productsize, name='pro-size'),
    path('productnames/', views.all_productsNames, name='pro-names'),
    path('customers/', views.all_customers, name='customer'),
    path('stockprop/', views.all_stock_prop, name='stock-prop'),
    path('works/', views.all_on_work, name='works'),
    path('addcart/', views.create_or_update_cart, name='works'),
    path('updatecart/<str:pk>/', views.update_cart, name='updatecart'),
    path('createproduct/', views.create_product, name='create-product'),
    path('addproduct/', views.add_product, name='add-product'),
    path('createstock/', views.create_stock, name='create-stock'),
    path('createemployee/', views.create_employee, name='create-employee'),
    path('deleteemployee/<str:pk>/', views.delete_employee, name='delete-employee'),
    path('updateemployee/<str:pk>/', views.update_employee, name='update-employee'),
    path('complete/<str:pk>/', views.update_work, name='update-work'),
    path('updateproduct/<str:pk>/', views.update_product, name='update-product'),
    path('updatestock/<str:pk>/', views.update_stock, name='update-stock'),
    path('reset/<str:pk>/', views.reset_expense, name='update-expense'),
    path('createprogress/', views.create_progress, name='create_progress'),
    path('expenses/', views.all_expenses, name='expenses'),
    path('createexpenses/', views.create_or_update_expenses, name='create-expenses'),
    path('fastmovingproduct/', views.fast_moving_products_api, name='fast-moving-product'),
    path('register/', views.user_registration, name='user-registration'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
