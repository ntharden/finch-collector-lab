from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('friends/', views.friends_index, name='friends_index'),
  path('friends/<int:friend_id>/', views.friends_detail, name='friends_detail'),
  path('friends/create/', views.FriendCreate.as_view(), name='friends_create'),
  path('friends/update/', views.FriendUpdate.as_view(), name='friends_update'),
  path('friends/delete/', views.FriendDelete.as_view(), name='friends_delete'),
  path('friends/<int:friend_id>/add_order/', views.add_order, name='add_order'),
]