from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail'),
    path('book_delete/<int:book_id>', views.book_delete, name='book_delete'),
    path('postbook', views.postbook, name='postbook'),
    path('displaybooks', views.displaybooks, name='displaybooks'),
    path('mybooks', views.mybooks, name='mybooks'),
    path('search', views.search_results, name='search_results'),
    path('leave_review/<int:book_id>', views.leave_review, name='leave_review'),
    path('view_reviews', views.view_reviews, name='view_reviews'),
    path('profile', views.profile, name='profile'),
]
