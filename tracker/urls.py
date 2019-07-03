from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.user_home, name='user-home'),
    path('habit/<pk>', views.habit_detail, name='habit-detail'),
    path('new_habit/', views.create_habit, name='new-habit'),
    path('habit/<pk>/delete/', views.delete_habit, name='delete'),
    path('habit/<pk>/add_record/', views.add_record, name='add-record'),
    path('habit/<pk>/add_observer/', views.add_observer, name='add-observer'),
]
