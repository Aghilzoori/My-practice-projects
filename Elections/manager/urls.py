from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('creat-candidate/', views.creat_candidate, name='creat-candidate'),
    path('edit-candidate/<int:pk>/', views.edit_candidate, name='edit-candidate'),
    path('delete-candidate/<int:pk>/', views.delete_candidate, name='delete-candidate'),
    path("export/", views.export_excel, name="export_excel")
]
