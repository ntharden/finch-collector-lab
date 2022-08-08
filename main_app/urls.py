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
  path('items/create/', views.ItemCreate.as_view(), name='items_create'),
  path('items/<int:pk>/', views.ItemDetail.as_view(), name='items_detail'),
  path('items/', views.ItemList.as_view(), name='items_index'),
  path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
  path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
  path('friends/<int:friend_id>/assoc_item/<int:item_id>/', views.assoc_item, name='assoc_item'),
  path('', views.Home.as_view(), name='home'),
  path('accounts/signup/', views.signup, name='signup'),
]