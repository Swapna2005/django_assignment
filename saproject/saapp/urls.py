from django.urls import path
from .views import add_book, BookListView
from . import views 
from .views import login_view


urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', login_view, name='registration/login'), 
    path('logout/', views.logout_view, name='logout'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('add-book/', add_book, name='add-book'),
  
]