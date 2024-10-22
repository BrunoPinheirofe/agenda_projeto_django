from django.urls import path

from contact import views
from contact.views import user_forms

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/', views.contact, name='contact'),
    path('', views.index, name='index'),
    
    
    #CRUD
    path('search/', views.search, name='search'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    
    
    #User
    path('user/create/', views.register,name='register'),
    path('user/update/', views.user_update, name='user_update'),
    path('user/login/', views.login_view, name = 'login'),
    path('user/logout/', views.logout_view, name = 'logout')
    
    
] 