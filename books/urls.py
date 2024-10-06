from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('', views.book_list, name='book_list'),
    path('return/<int:book_id>/', views.return_book, name='return_book'),
]
