from django.urls import path
from . import views


urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name='menu_item'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]