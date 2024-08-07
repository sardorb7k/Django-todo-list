from django.urls import path
from blog.views import index, update_todo, delete_todo, complete_todo

urlpatterns = [
    path('', index, name='index'),
    path('update/<int:pk>/', update_todo, name='update_todo'),
    path('delete/<int:pk>/', delete_todo, name='delete_todo'),
    path('complete/<int:pk>/', complete_todo, name='complete_todo'),
]
