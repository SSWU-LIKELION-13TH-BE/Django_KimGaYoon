from django.contrib import admin
from django.urls import include, path
from django.urls import path
from .views import signup_view, login_view, logout_view, home_view, password_reset_view, update_profile_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),  
    path('password-reset/', password_reset_view, name='password_reset'),
    path('update-profile/', update_profile_view, name='update_profile'),
    
    #path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  
    #path('admin/', admin.site.urls),  # admin 네임스페이스 등록
    
]