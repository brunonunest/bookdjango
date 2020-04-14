from django.urls import path, include
from accounts import views
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('', views.IndexView, name='home'),
    path('register/', views.RegisterView, name='register_url'),
    path('dashboard/', views.DashboardView, name='login_url'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='dashboard/'), name='logout'),
]