from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Friend, Item
from .forms import OrderForm

class Friend:
  def __init__(self, name, job, description):
    self.name = name
    self.job = job
    self.description = description

class FriendCreate(LoginRequiredMixin, CreateView):
  model = Friend
  fields = ['name', 'job', 'description']
  success_url = '/friends/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FriendUpdate(LoginRequiredMixin, UpdateView):
  model = Friend
  fields = '__all__'

class FriendDelete(LoginRequiredMixin, DeleteView):
  model = Friend
  success_url = '/friends/'
  
class ItemCreate(LoginRequiredMixin, CreateView):
  model = Item
  fields = '__all__'

class ItemList(LoginRequiredMixin, ListView):
  model = Item

class ItemDetail(LoginRequiredMixin, DetailView):
  model = Item

class ItemUpdate(LoginRequiredMixin, UpdateView):
  model = Item
  fields = ['name', 'color']

class ItemDelete(LoginRequiredMixin, DeleteView):
  model = Item
  success_url = '/items/'

class Home(LoginView):
  template_name = 'home.html'

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

@login_required
def friends_index(request):
  friends = Friend.objects.filter(user=request.user)
  return render(request, 'friends/index.html', { 'friends': friends })

@login_required
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

@login_required
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('friends_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)