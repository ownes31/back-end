from django.urls import path
from . import views  # ✅ Импортируем views из приложения post

urlpatterns = [
    path("", views.redirect_to_threads, name="home"),
    path("threads/", views.thread_list, name="thread_list"),
    path("threads/create/", views.thread_create, name="thread_create"),
    path("threads/my/", views.my_threads, name="my_threads"),

]
