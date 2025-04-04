from django.urls import path
from .views import signup_view, login_view, logout_view, home_view, password_reset_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),  
    path('password_reset/', password_reset_view, name='password_reset'),
]