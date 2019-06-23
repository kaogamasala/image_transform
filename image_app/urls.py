from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'image_app'
urlpatterns = [
    path('',views.index, name="index"),
    path('users_detail/<int:pk>/', views.users_detail, name='users_detail'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='image_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]