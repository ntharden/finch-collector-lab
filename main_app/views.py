from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Friend, Item
from .forms import OrderForm

class Friend:
  def __init__(self, name, job, description):
    self.name = name
    self.job = job
    self.description = description

class FriendCreate(CreateView):
  model = Friend
  fields = ['name', 'job', 'description']
  success_url = '/friends/'

class FriendUpdate(UpdateView):
  model = Friend
  fields = '__all__'

class FriendDelete(DeleteView):
  model = Friend
  success_url = '/friends/'
  
class ItemCreate(CreateView):
  model = Item
  fields = '__all__'

class ItemList(ListView):
  model = Item

class ItemDetail(DetailView):
  model = Item

class ItemUpdate(UpdateView):
  model = Item
  fields = ['name', 'color']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/items/'

friends = [
  Friend('Joey', 'doctor/actor', 'Likes girls. Loves to eat.'),
  Friend('Phoebe', 'masseuse', 'In touch with the supernatural.'),
  Friend('Ross', 'paleontologist', 'Great mover. Skilled on the keys'),
  Friend('Rachel', 'fashion designer', 'Mischevious but caring.'),
  Friend('Chandler', 'accountant', 'Dance is my life.'),
  Friend('Monica', 'chef', 'Neat and organized.'),
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def friends_index(request):
  friends = Friend.objects.all()
  return render(request, 'friends/index.html', { 'friends': friends })

def friends_detail(request, friend_id):
  friend = Friend.objects.get(id=friend_id)
  items_friend_doesnt_have = Friend.objects.exclude(id__in = friend.items.all().values_list('id'))
  order_form = OrderForm()
  return render(
    request,
    'friends/detail.html',
    { 'friend': friend },
    { 'order_form': order_form },
    { 'items': items_friend_doesnt_have }
  )

def add_order(request, friend_id):
  form = OrderForm(request.POST)
  if form.is_valid():
    new_order.friend_id = form.save(commit=False)
    new_order.friend_id = friend_id
    new_order.save()
  return redirect('friends_detail', friend_id=friend_id)

def assoc_item(request, friend_id, item_id):
  Friend.objects.get(id=friend_id).items.add(item_id)
  return redirect('friends_detail', friend_id=friend_id)