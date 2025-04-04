from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

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


'''
def password_reset_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        # 비밀번호 초기화 로직 추가
        return redirect('login')  # 비밀번호 초기화 후 이동할 URL
    return render(request, "password_reset.html")

from django.core.mail import send_mail
from django.http import HttpResponse

def send_email(request):
    if request.method == "POST":
        subject = "비밀번호 재설정 요청"
        message = "비밀번호를 재설정하려면 아래 링크를 클릭하세요."
        from_email = "20221188@sungshin.ac.kr"  # 발신 이메일
        recipient_list = [request.POST.get("email")]  # 사용자가 입력한 이메일

        try:
            send_mail(subject, message, from_email, recipient_list)
            return HttpResponse("이메일이 성공적으로 전송되었습니다.")  # 성공 메시지 반환
        except Exception as e:
            return HttpResponse(f"이메일 전송에 실패했습니다: {e}")  # 실패 메시지 반환

    return render(request, "password_reset.html")  # GET 요청 시 템플릿 렌더링
'''
# 비밀번호 찾기 (아이디와 이메일을 입력받고 비밀번호 변경)
def password_reset_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')

        try:
            # 사용자가 입력한 username과 email로 유저 찾기
            user = User.objects.get(username=username, email=email)

            # 비밀번호 유효성 검사를 여기에 추가 가능
            if len(new_password) < 8:
                messages.error(request, '비밀번호는 최소 8자 이상이어야 합니다.')
                return redirect('password_reset')

            # 비밀번호 변경
            user.set_password(new_password)  # 비밀번호 변경
            user.save()

            messages.success(request, '비밀번호가 성공적으로 변경되었습니다.')
            return redirect('login')  # 로그인 페이지로 리디렉션

        except User.DoesNotExist:
            messages.error(request, '아이디와 이메일이 일치하지 않습니다.')
            return redirect('password_reset')

    return render(request, 'password_reset.html')

# Create your views here.
#render랑 redirect의 차이
