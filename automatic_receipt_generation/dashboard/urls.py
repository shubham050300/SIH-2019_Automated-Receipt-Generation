from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard_home, name = 'dashboard_home'),
    url(r'^sent/', views.sent, name='sent'),
]