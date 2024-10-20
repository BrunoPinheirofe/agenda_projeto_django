from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),
    path('', views.index, name='index'),
    
    
    #CRUD
    path('search/', views.search, name='search'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    
] 