# 카카오 계정 연동



## allauth 설정

- allauth 설치

    ```bash
    $ pip install allauth
    ```

- `settings.py` 에 추가

    [reference](<https://django-allauth.readthedocs.io/en/latest/installation.html#post-installation>)

    ```python
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    )
    
    INSTALLED_APPS = (
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.kakao',
    ```

- `url.py` > `urlpatterns` 에 추가

    ```python
    path('accounts/', include('allauth.urls')),
    ```



### KakaoDevelpoers 사이트에서 앱 등록

- [Kakao developer](<https://developers.kakao.com/>) 사이트에 가입하기

- 새로운 앱 만들기 후 앱명과 회사명 입력

- 설정 > 일반 > 플랫폼 추가 > 도메인 2개 추가

    ```url
    http://127.0.0.1:8000
    https://127.0.0.1:8000
    ```

- Redirect Path 설정 후 저장

  ```redirect path
  /accounts/kakao/login/callback/
  ```

- 고급 > Client Secret 키 발급받기

    - 상태 `ON` 으로 하고 적용

- 사용자 관리 탭에서 사용자 관리 활성화
  - 프로필 정보, 카카오계정 수집 내용 입력



### admin 페이지에서 다음 입력



### `accounts/login.html` 변경

```html
{% extends 'boards/base.html' %}
{% load bootstrap4 %}
{% load socialaccount %}

{% block body %}
<h1>로그인</h1>
<form action="" method="post">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons submit="로그인" reset="Cancel" %}{% endbuttons %}
</form>
<a href="{% provider_login_url 'kakao' method='oauth2' %}" class="btn btn-warning">카카오 로그인</a>
{% endblock %}
```



### 로그인 후 index 페이지로 redirect 되도록 설정

`settings.py` 에서 추가

```python
LOGIN_REDIRECT_URL = 'boards:index'
```



### 계정 생성시 충돌 문제 해결

`settings.py` 수정

```python
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',  <- 주석처리
)
```

