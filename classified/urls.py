from django.urls import path
from classified import views

urlpatterns = [
    path('list/', views.ClassifiedList.as_view(), name='list'),
    path('<int:pk>/', views.ClassifiedDetail.as_view(), name='detail'),
]