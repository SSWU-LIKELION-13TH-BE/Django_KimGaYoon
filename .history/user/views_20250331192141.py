from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # 로그인 성공 시 이동할 URL
        else:
            return render(request, "login.html", {"error": "로그인 정보가 올바르지 않습니다."})
    return render(request, "login.html")

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # 로그아웃 후 이동할 URL
    return render(request, "logout.html")
    
def home_view(request):
    return render(request, 'home.html')  # 로그인 성공 시 이동할 URL
def password_reset_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        # 비밀번호 초기화 로직 추가
        return redirect('login')  # 비밀번호 초기화 후 이동할 URL
    return render(request, "password_reset.html")

# Create your views here.
#render랑 redirect의 차이
