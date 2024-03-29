from django.urls import path
from .views import users_list, book_list

urlpatterns = [
    path('users/', users_list),
    path('book_list/', book_list),
]