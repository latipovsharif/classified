from django.urls import path
from classified import views

urlpatterns = [
    path('list/', views.classfield_list)
]