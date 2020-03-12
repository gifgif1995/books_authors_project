from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.books), 
    path('add_book', views.add_book), 
    path('books/<book_id>/', views.view_book), 
    path('add_auth_to_book/<book_id>', views.add_auth_to_book), 
    path('authors/', views.authors), 
    path('add_author', views.add_author), 
    path('authors/<author_id>/', views.view_author), 
    path('add_book_to_auth/<author_id>', views.add_book_to_auth) 
]