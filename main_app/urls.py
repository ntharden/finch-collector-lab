from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('friends/', views.friends_index, name='friends_index'),
  path('friends/<int:friend_id>/', views.friends_detail, name='friends_detail'),
]