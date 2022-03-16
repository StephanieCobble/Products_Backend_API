from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns 
from .import views

urlpatterns = [
    path('', views.ReviewList.as_view()),
    path('<int:pk>/', views.ReviewDetail.as_view()),
    path('fk/<int:fk>/', views.ReviewFK.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)

