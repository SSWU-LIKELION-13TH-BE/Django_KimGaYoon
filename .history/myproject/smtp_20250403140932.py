import smtplib

try:
    # SMTP 서버 연결
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # TLS 보안 시작
    server.login('20221188@sungshin.ac.kr', 'robs ndrj gcdu ugog')  # 이메일 계정과 앱 비밀번호
    print("SMTP 서버 연결 성공")
except Exception as e:
    print(f"SMTP 서버 연결 실패: {e}")
finally:
    server.quit()  # 연결 종료