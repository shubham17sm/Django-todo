from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('add/', views.add_task, name='add'),
    path('delete/<pk>/', views.delete_task, name='delete'),
    path('deleteall/', views.delete_all_tasks, name='deleteall'),
    path('complete/<pk>/', views.complete_task, name='complete'),
    path('deletecompleted/', views.delete_all_complete, name='allcompletedel'),
]