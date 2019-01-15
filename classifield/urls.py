from django.urls import path
from classifield import views

urlpatterns = [
    path('list/', views.list)
]