from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns #added import
from .import views

# urlpatterns = [
#     path('', views.products_list),
#     path('<int:pk>/', views.product_detail),
# ]


urlpatterns = [
    path('', views.ProductList.as_view()),
    path('<int:pk>/', views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)