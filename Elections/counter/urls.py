from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path('counter/', views.vote_user, name="vote_user")
]
