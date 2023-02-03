
from django.urls import path

app_name = 'accounts'

from . import views

urlpatterns = [
    path('cadastrar', views.home, name='cadastrar_usuario'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout')
]

