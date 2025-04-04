from django.urls import path
from .views import signup_view, login_view, logout_view, home_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),  # 로그인 성공 시 이동할 URL
]