from django.urls import path
from .views import *

urlpatterns = [
  path('',home, name = 'index'),
  path('generals/', generals, name = 'generals'),
  path('contact/', contact, name = 'contact'),
  path('news/', news, name = 'news'),
  path('<slug:slug>/', detailPost, name = 'detail_post'),
  
]