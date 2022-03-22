from django.urls import path
from .views import home , detail, category
urlpatterns = [
  path('', home, name='home'),
  path('detail/<slug:slug>', detail, name='detail'),
  path('category/<slug:slug>', category, name='category'),

]
