# Django로 게시판 만들기 (1)



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



## 게시글 수정 기능

1. `boards/url.py`에 추가

   ```python
   path('<int:id>/edit/', views.edit),  # 게시글 수정 페이지 렌더링
   ```

2. `boards/views.py` 에 추가

   ```python
   # 게시글 수정 페이지 렌더링
   def edit(request, id):
       # id 값에 맞는 board 데이터 꺼낸 후 edit.html 로 넘기기
       board = Board.objects.get(id=id)
       context = {'board': board}
       return render(request, 'boards/edit.html', context)
   ```

3. `boards/templates/boards/edit.html` 생성 ( `new.html` 과 비슷하게 )

   ```html
   {% extends 'boards/base.html' %}
   
   {% block body %}
       <h1>EDIT</h1>
       <form action="/boards/{{board.id}}/update/" method="post">
           {% csrf_token %}  <!-- csrf 토큰을 함께 보낸다 -->
           <label for="title">Title</label><br />
           <input id="title" type="text" name="title"
                  value="{{board.title}}"><br />
           <label for="content">Content</label><br />
           <textarea name="content" id="content">
               {{board.content}}
           </textarea><br />
           <input type="submit">
       </form>
       <a href="/boards/">돌아가기</a>
   {% endblock %}
   ```

4. `boards/urls.py` 에 update를 처리할 url 추가

   ```python
   path('<int:id>/update/', views.update)  # 사용자가 입력한 수정 데이터를 전송받고 실제 DB 에 수정 후 저장
   ```

5. `boards/views.py` 에 update 처리 메소드 작성

   ```python
   def update(request, id):
       title = request.POST.get('title')
       content = request.POST.get('content')
       # id 값에 맞는 board 데이터를 위에서 주어진 title 과 content에 맞게
       # 수정한 뒤 저장하는로직
       # 1. Board 클래스를 통해 id 값에 맞는 데이터를 가져온다.
       board = Board.objects.get(id=id)
   
       # 2. 해당 데이터의 내용을 주어진 title, content 로 수정한다.
       board.title = title
       board.content = content
   
       # 3. 저장한다.
       board.save()
   
       return redirect(f'/boards/{id}/')
   ```

6. `boards/templates/boards/detail.html` 에 edit.html 연결 링크 추가

   ```html
   <p>
       <a href="/boards/{{board.id}}/edit">EDIT</a>
   </p>
   ```



## URL에 name을 명시하여 사후관리 용이하게 하기

1. `boards/urls.py` 수정

   ```python
   app_name = 'boards'  # boards app 임을 명시
   
   urlpatterns = [
       path('', views.index, name='index'),
       path('new/', views.new, name='new'),
       path('create/', views.create, name='create'),
       path('<int:id>/', views.detail, name='detail'),
       path('<int:id>/delete/', views.delete, name='delete'),
       path('<int:id>/edit/', views.edit, name='edit'),
       path('<int:id>/update/', views.update, name='update'),
   ]
   ```

2. `boards/views.py` 수정 (redirect 부분을 바꿔준다.)

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
       print('new board id: ', board.id)
       return redirect('boards:detail', board.id)
   
   
   # 특정 게시글 하나만 가지고 온다.
   def detail(request, id):
       # Board 클래스를 사용해서 id 값에 맞는 데이터를 가지고 온다.
       # context 로 넘겨서 detail.html 페이지에서 title 과 content 를 출력해본다.
       board = Board.objects.get(id=id)
       context = {'board': board}
       return render(request, 'boards/detail.html', context)
   
   
   # 특정 게시글 삭제
   def delete(request, id):
       board = Board.objects.get(id=id)
       board.delete()
       return redirect('boards:index')
   
   
   # 게시글 수정 페이지 렌더링
   def edit(request, id):
       # id 값에 맞는 board 데이터 꺼낸 후 edit.html 로 넘기기
       board = Board.objects.get(id=id)
       context = {'board': board}
       return render(request, 'boards/edit.html', context)
   
   
   def update(request, id):
       title = request.POST.get('title')
       content = request.POST.get('content')
       # id 값에 맞는 board 데이터를 위에서 주어진 title 과 content에 맞게
       # 수정한 뒤 저장하는로직
       # 1. Board 클래스를 통해 id 값에 맞는 데이터를 가져온다.
       board = Board.objects.get(id=id)
   
       # 2. 해당 데이터의 내용을 주어진 title, content 로 수정한다.
       board.title = title
       board.content = content
   
       # 3. 저장한다.
       board.save()
   
       return redirect('boards:detail', id)
   ```

3. html 코드에서도 url 수정 (아래는 index.html 예시. 다른 html 파일도 수정해야함)

   ```html
   {% extends 'boards/base.html' %}  <!-- base.html 을 상속받음 -->
   
   {% block body %}  <!-- /base.html 안의 block body 부분에 내용이 들어간다. -->
       <h1>Welcome to boards</h1>
       <hr />
       {% for board in boards %}
           {{ board.id }} | <a href="{% url 'boards:detail' board.id %}">{{ board.title }}</a>
           <hr />
       {% endfor %}
       <a href="{% url 'boards:new' %}">새로운 글 작성</a>
   {% endblock %}
   ```



## admin 페이지 생성

1. 관리자 계정 생성

   ```bash
   $ python manage.py createsuperuser
   ```

2. `boards/admin.py` 수정

   ```python
   from django.contrib import admin
   from .models import Board
   
   # Register your models here.
   admin.site.register(Board)
   ```

3. `boards/models.py` 의 Board class 안에 다음 코드 추가

   ```python
   def __str__(self):
       # 형식 예: 1. 첫번째 포스트
       return f'{self.id}. {self.title}'
   ```



## Restful하게 코드 변경

- Request 방법의 종류

  ```
  GET			/boards/<id>/
  POST		/boards/<id>/
  PUT(PATCH)	/boards/<id>/
  DELETE		/boards/<id>/
  ```

- Django에서는 GET과 POST 두 가지 방법만 제공한다.

  ```
  GET			/boards/<id>/
  POST		/boards/<id>/
  POST		/boards/<id>/edit
  POST		/boards/<id>/delete
  ```

- `boards/views.py` new 메소드 부분 수정

  ```python
  def new(request):
      # GET
      if request.method == 'GET':
          return render(request, 'boards/new.html')
      # POST
      else:
          title = request.POST.get('title')
          content = request.POST.get('content')
          board = Board(title=title, content=content)
          board.save()
          print('new board id: ', board.id)
          return redirect('boards:detail', board.id)
  ```

- `boards/templates/boards/new.html` 페이지에서 `/boards/new/` 으로 post 방식으로 요청하도록 수정

  ```html
  <form action="{% url 'boards:new' %}" method="post">
  ```

- 필요없어진 create.html과 url, view 함수 제거

- 같은 방식으로 edit view 수정하기

  `boards/views.py`

  ```python
  def edit(request, id):
      board = Board.objects.get(id=id)  # DRY (Don't Repeat Yourself)
      # GET
      if request.method == 'GET':
          context = {'board': board}
          return render(request, 'boards/edit.html', context)
      # POST
      else:
          title = request.POST.get('title')
          content = request.POST.get('content')
          board.title = title
          board.content = content
          board.save()
          return redirect('boards:detail', id)
  ```

  `boards/templates/boards/edit.html`

  ```html
  <form action="{% url 'boards:edit' board.id %}" method="post">
  ```

  `boards/urls.py`

  ```python
  urlpatterns = [
      path('', views.index, name='index'),
      path('new/', views.new, name='new'),
      path('<int:id>/', views.detail, name='detail'),
      path('<int:id>/delete/', views.delete, name='delete'),
      path('<int:id>/edit/', views.edit, name='edit'),
  ]
  ```

- url에 직접 요청하는 방법 (GET 방식) 으로 게시글을 삭제하지 못하도록 수정

  `boards/views.py`

  ```python
  from django.views.decorators.http import require_http_methods
  
  # 특정 게시글 삭제
  @require_http_methods(['POST'])  # 허용할 request 방식을 리스트에 담음.
  def delete(request, id):         # GET 요청을 받으면 status 405 error code 를 전달
      board = Board.objects.get(id=id)
      board.delete()
      return redirect('boards:index')
  ```

- 다른 함수에도 @require_http_methods로 접근방법을 한정시킨다.



## 존재하지 않는 페이지 접근 시 404 error 전달하기

- `boards/views.py` 에서 get_object_or_404 메서드 추가

  ```python
  from django.shortcuts import render, redirect, get_object_or_404
  ```

- `boards/views.py` 에서

  `board = Board.objects.get(id=id)` 코드를 모두 찾아 다음과 같이 수정

  ```python
  board = get_object_or_404(Board, id=id)
  ```

