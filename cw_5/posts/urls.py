from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/my/', views.my_posts, name='my_posts'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),
]
