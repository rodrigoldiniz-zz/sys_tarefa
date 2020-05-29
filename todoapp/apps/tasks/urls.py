from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
               path('categorias/', views.list_categories, name='list_categories'),
               path('categorias/adicionar/', views.add_category, name='add_category'),
               path('categorias/editar/<int:id_category>/', views.edit_category, name='edit_category'),
               path('categorias/excluir/<int:id_category>/', views.delete_category, name='delete_category'),
               ]
