# Django로 게시판 만들기



## Django 설치 및 기본 설정

1. Django 설치

   ```bash
   $ pip install django
   ```

2. Django project 생성

   ```bash
   $ django-admin startproject curd .
   ```

3. Django app 생성

   ```bash
   $ python manage.py startapp boards
   ```

4. `crud/settings.py` 변경

   ```python
   INSTALLED_APPS = [
       # Local Apps
       'boards',  # <- 추가
       
       # Django Apps
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
   ]
   
   ...
   
   LANGUAGE_CODE = 'ko-kr'  # <- 변경
   
   TIME_ZONE = 'Asia/Seoul'  # <- 변경
   ```



## 기본 url 설정

1. `crud/urls.py` 변경

   ```python
   from django.contrib import admin
   from django.urls import path, include  # <- 추가
   
   urlpatterns = [
       path('boards/', include('boards.urls')),  # boards > urls.py <- 추가
       path('admin/', admin.site.urls),
   ]
   ```

2. `boards/urls.py` 생성 및 작성

   ```python
   from django.urls import path
   
   urlpatterns = [
       path(''),  # www.mulcam.com/boards/
   ]
   ```

3. `boards/views.py` 변경

   ```python
   from django.shortcuts import render
   
   
   # Create your views here.
   def index(request):
       return render(request, 'boards/index.html')
   ```

4. `boards/urls.py` 변경

   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('', views.index),  # www.mulcam.com/boards/
   ]
   ```

5. `boards/templates/boards/base.html` 생성 (나중에 다른 페이지가 이 페이지를 상속받아서 사용)

   ```html
   <!-- boards/base.html -->
   
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
       <title>CRUD</title>
   </head>
   <body>
       <div class="container">
           {% block body %}  <!-- 이 안에서 상속받은 페이지가 나타남 -->
           {% endblock %}
       </div>
       <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
       <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
       <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

6. `boards/templates/boards/index.html` 생성

   ```html
   {% extends 'boards/base.html' %}  <!-- base.html 을 상속받음 -->
   
   {% block body %}  <!-- /base.html 안의 block body 부분에 내용이 들어간다. -->
       <h1>Welcome to boards</h1>
   {% endblock %}
   ```

   

## Model 설정 (DB 생성)

1. `boards/models.py` 변경

   ```python
   from django.db import models
   
   
   # Create your models here.
   class Board(models.Model):
       title = models.CharField(max_length=20)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)  # 데이터가 생성되는 시점의 시간과 날짜가 자동으로 입력됨
       updated_at = models.DateTimeField(auto_now=True)  # 데이터의 조작이 가해지는 시점의 시간과 날짜가 자동으로 입력됨
   ```

2. migrations 생성

   ```bash
   $ python manage.py makemigrations
   ```

3. migrate 명령으로 `boards/models.py`에 작성한 내용 반영

   ```bash
   $ python manage.py migrate
   ```



## 입력페이지 작성

1. `boards/urls.py ` 에 추가

   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('', views.index),  # www.mulcam.com/boards/
       path('new/', views.new),  # 사용자의 입력을 받아서 게시글을 작성하는 곳
       path('create/', views.create),  # 사용자가 입력한 데이터를 전송받고
       								# 실제 DB에 작성 및 사용자 피드백
   ]
   ```

2. `boards/views.py` 에 추가

   ```python
   from django.shortcuts import render, redirect
   
   # 사용자 입력을 받는 페이지 렌터링
   def new(request):
       return render(request, 'boards/new.html')
   
   
   def create(request):
       return render(request)
   ```

3. `boards/templates/boards/new.html` 생성

   ```html
   {% extends 'boards/base.html' %}
   
   {% block body %}
       <h1>NEW</h1>
   	{% csrf_token %}
       <form action="/boards/create/" method="post">
           <label for="title">Title</label><br />
           <input id="title" type="text" name="title"><br />
           <label for="content">Content</label><br />
           <textarea name="content" id="content"></textarea><br />
           <input type="submit">
       </form>
   {% endblock %}
   ```

   REST (Representational State Trasfer)

   - GET: 가지고 와라
   - POST: 작성을 하겠다
   - PUT: 수정을 하겠다
   - DELETE: 삭제를 하겠다

4. `boards/views.py` 변경

   ```python
   # 데이터를 받아서 실제 DB 에 작성
   def create(request):
       title = request.POST.get('title')
       content = request.POST.get('content')
       return redirect('/boards/')
   ```



## 입력받은 데이터 DB에 저장 후 불러오기

1. `boards/views.py` 변경

   ```python
   from django.shortcuts import render, redirect
   from .models import Board
   
   
   # Create your views here.
   def index(request):
       # Board 의 전체 데이터를 불러온다 - QuerySet
       boards = Board.objects.all()
       context = {'boards': boards}
       return render(request, 'boards/index.html', context)
   
   
   # 사용자 입력을 받는 페이지 렌터링
   def new(request):
       return render(request, 'boards/new.html')
   
   
   # 데이터를 받아서 실제 DB 에 작성
   def create(request):
       title = request.POST.get('title')
       content = request.POST.get('content')
       board = Board(title=title, content=content)
       board.save()
       return redirect('/boards/')
   ```

2. `boards/templates/boards/index.html` 변경

   ```html
   {% extends 'boards/base.html' %}  <!-- base.html 을 상속받음 -->
   
   {% block body %}  <!-- /base.html 안의 block body 부분에 내용이 들어간다. -->
       <h1>Welcome to boards</h1>
       <hr />
       {% for board in boards %}
           <p>글 번호 : {{ board.id }}</p>
           <p>글 제목 : {{ board.title }}</p>
           <p>글 내용 : {{ board.content }}</p>
           <hr />
       {% endfor %}
       <a href="/boards/new/">새로운 글 작성</a>
   {% endblock %}
   ```



## 특정 게시글 불러오기

1. `boards/urls.py` 에 특정 게시글을 불러오는 url 추가

   ```python
   path('<int:id>/', views.detail),  # www.mulcam.com/boards/<id>/  <id>는 동적으로 id 값이 들어온다.
   ```

2. `boards/views.py` 에 detail 페이지 뷰 작성

   ```python
   # 특정 게시글 하나만 가지고 온다.
   def detail(request, id):
       # Board 클래스를 사용해서 id 값에 맞는 데이터를 가지고 온다.
       # context 로 넘겨서 detail.html 페이지에서 title 과 content 를 출력해본다.
       board = Board.objects.get(id=id)
       context = {'board': board}
       return render(request, 'boards/detail.html', context)
   ```

3. `boards/templates/boards/detail.html` 생성

   ```html
   {% extends 'boards/base.html' %}
   
   {% block body %}
       <h1>Detail</h1>
       <h2>{{ board.title }}</h2>
       <p>{{ board.id }}번째 글</p>
       <p>{{ board.created_at }}</p>
       <hr />
       <p>{{ board.content }}</p>
   {% endblock %}
   ```

4. `boards/templates/boards/index.html` 수정

   ```html
   {% extends 'boards/base.html' %}  <!-- base.html 을 상속받음 -->
   
   {% block body %}  <!-- /base.html 안의 block body 부분에 내용이 들어간다. -->
       <h1>Welcome to boards</h1>
       <hr />
       {% for board in boards %}
           <a href="/boards/{{board.id}}">{{ board.id }} | {{ board.title }}</a>
           <hr />
       {% endfor %}
       <a href="/boards/new/">새로운 글 작성</a>
   {% endblock %}
   ```

5. 게시글 생성 시 `boards/templates/boards/detail.html` 로 redirect 되도록 수정

   ```python
   # 데이터를 받아서 실제 DB 에 작성
   def create(request):
       title = request.POST.get('title')
       content = request.POST.get('content')
       board = Board(title=title, content=content)
       board.save()
       print('new board id: ', board.id)
       return redirect(f'/boards/{board.id}/')
   ```



## 게시글 삭제 기능

1. `boards/urls.py` 에 추가

   ```python
   path('<int:id>/delete/', views.delete)
   ```

2. `boards/views.py` 에 추가

   ```python
   # 특정 게시글 삭제
   def delete(request, id):
       board = Board.objects.get(id=id)
       board.delete()
       return redirect('/boards/')
   ```

3. `boards/templates/boards/detail.html` 에서 `/board/<id>/delete/` 를 호출하는 링크 추가

   ```html
   <p>
   	<form action="/boards/{{board.id}}/delete/" method="post">
   		{% csrf_token %}
   		<input class="btn btn-danger" type="submit" value="DELETE"/>
   	</form>
   </p>
   ```

