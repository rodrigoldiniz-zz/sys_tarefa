from django.urls import path
from . import views


app_name = 'accounts'


urlpatterns = [
    path('novo-usuario/', views.add_user, name='add_user'),
    path('login/', views.user_login, name='user_login'),
]
