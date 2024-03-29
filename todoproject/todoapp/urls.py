from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.add,name='home'),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update, name="update"),
    path('cbvhome/',views.TasklistView.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),


]