from django.shortcuts import render
from .models import Friend

class Friend:
  def __init__(self, name, job, description):
    self.name = name
    self.job = job
    self.description = description

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
  return render(request, 'friends/detail.html', { 'friend': friend })
