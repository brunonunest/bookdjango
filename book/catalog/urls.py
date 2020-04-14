from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'catalog', views.BookView)
#router.register(r'accounts', views.IndexView, name='home')


#router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]