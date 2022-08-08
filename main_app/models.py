from ast import FloorDiv
from django.db import models
from django.urls import reverse
from datetime import date

DRINKS = (
  ('C','Coffee'),
  ('B','Beer')
)

FOODS = (
  ('T','Turkey'),
  ('S','Spaghetti')
)

class Item(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('items_detail', kwargs={'pk': self.id})

class Friend(models.Model):
  name = models.CharField(max_length=100)
  job = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  items = models.ManyToManyField(Item)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse("friends_detail", kwargs={"friend_id": self.id})
  def ordered_for_today(self):
    return self.order_set.filter(date=date.today()).count() >= len(DRINKS)
  
class Order(models.Model):
  date = models.DateField('Order date')
  drink = models.CharField(
    max_length=1,
    choices=DRINKS,
    default=DRINKS[0][0]
  )
  food = models.CharField(
    max_length=1,
    choices=FOODS,
    default=FOODS[0][0]
  )
  friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.get_drink_display()} to drink and {self.food()} to eat on {self.date}"
  class Meta:
    ordering = ['-date']
