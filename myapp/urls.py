from django.contrib.staticfiles.urls import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'), 
     path('', views.index, name='index'),  
    path('register/', views.register_user, name='register_user'),  # Привязываем URL '/register/' к представлению register_user
]
