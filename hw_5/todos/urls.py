from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todos/<int:id>/delete/', views.todo_delete, name='todo_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]


urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('<int:id>/', views.todo_detail, name='todo_detail'),
]
