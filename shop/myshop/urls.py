from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.home, name='home'),
    path('category', views.category, name='category'),
    path('products', views.all_products, name='products'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail')
]
