from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login_user"),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_view, name='logout'),
]