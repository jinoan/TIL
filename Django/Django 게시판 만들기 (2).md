# Django 게시판 만들기 (2)



## 댓글을 저장할 DB model 만들기

- `boards/models.py` 에 추가

  ```python
  class Comment(models.Model):
      content = models.TextField()  # 댓글의 내용
      created_at = models.DateTimeField(auto_now_add=True)  # 데이터가 생성되는 시점의 시간과 날짜가 자동으로 입력됨
      updated_at = models.DateTimeField(auto_now=True)  # 데이터의 조작이 가해지는 시점의 시간과 날짜가 자동으로 입력됨
      board = models.ForeignKey(Board, on_delete=models.CASCADE)
      # CASCADE는 외래키가 삭제되면 해당되는 데이터를 모두 삭제시킨다.
  ```

- makemigrations (DB의 설계도를 만드는 작업)

  ```bash
  $ python manage.py makemigrations
  ```

- migrate (설계도대로 DB 만듦)

  ```bash
  $ python manage.py migrate
  ```

- migrations 확인

  ```bash
  $ python manage.py showmigrations
  ```



## Shell plus 이용하기 

- django-extensions 설치

  ```bash
  $ pip install django-extensions
  ```

- `crud/settings.py` 안의 `INSTALLED_APPS` 리스트 안에 아래 코드 추가

  ```python
  # 3rd party Apps
  'django_extensions',
  ```

- Terminal에서 shell plus 열기

  ```bash
  $ python manage.py shell_plus
  ```

- 특정 게시글 불러오기

  ```python
  >>> board = Board.objects.get(pk=13)
  ```

- 댓글 생성

  ```python
  >>> comment = Comment()  # 인스턴스 생성
  >>> comment.content = '첫번째 댓글'  # 인스턴스 변수 할당
  >>> comment.board = board
  >>> comment.save()
  
  >>> comment.id  # 1
  >>> comment.board  # board 인스턴스 출력
  >>> comment.board_id  # 13
  >>> comment.board.title  # test
  ```

- 댓글 생성 2

  ```python
  >>> board = Board.objects.get(pk=18)
  >>> comment = Comment()
  >>> comment.content = '두번째 댓글입니다.'
  >>> comment.board_id = board.id
  >>> comment.board  # <Board: 18, test>
  ```

- 댓글 생성 3

  ```python
  >>> comment = Comment(board_id =board.id, content = '세번째 댓글입니다.')
  >>> comment.save()
  ```



## 표현 형식 변경

- `boards/models.py` 안의 Comment class에 아래 코드 추가

  ```python
  def __str__(self):
  	return f'<Board({self.board_id}): Comment({self.id}) - {self.content}>'
  ```

- shell plus 다시열기

  ```python
  >>> exit()
  ```

  ```bash
  $ python manage.py shell_plus
  ```

- comments 불러와서 확인

  ```python
  >>> comments = Comment.objects.all()
  >>> comments
  ```



## 보드에서 댓글 가져오기

- ```python
  >>> board = Board.objects.get(pk=13)
  >>> comments = board.comment_set.all()
  >>> comments  
  <QuerySet [<Comment: <Board(13): Comment(1) - 첫번째 댓글입니다.>>, <Comment: <Board(13): Comment(3) - 세번째 댓글입니다.>>]>
  ```



## Admin page에 comment 모델 등록

- `boards/admin.py`

  ```python
  from django.contrib import admin
  from .models import Board, Comment
  
  # Register your models here.
  admin.site.register(Board)
  admin.site.register(Comment)
  ```

- Admin page에 들어가서 확인

  ```bash
  $ python manage.py runserver
  ```

  브라우저 url에 `localhost:8000/admin/` 을 입력하여 들어간다.

- 관리자 계정이 없는 경우 아래 코드를 쳐서 id, email(생략 가능), password 등록

  ```bash
  $ python manage.py createsuperuer
  ```

  

  ## Comments 관련 url 작성

- `boards/urls.py` 에서 가독성을 위해 기존 id를 board_id로 변경

  ```python
  urlpatterns = [
      path('', views.index, name='index'),
      path('new/', views.new, name='new'),
      path('<int:board_id>/', views.detail, name='detail'),
      path('<int:board_id>/delete/', views.delete, name='delete'),
      path('<int:board_id>/edit/', views.edit, name='edit'),
  ]
  ```

- `boards/views.py` 에서도 url id에 해당되는 부분을 board_id로 변경

- `boards/urls.py` 에서 urlpatterns 리스트 안에 아래 코드 추가

  ```python
  # Comments
  path('<int:board_id>/comments/', views.comment_create, name='comment_create')
  ```

  

## Comment 생성 view 작성

- `boards/views.py` 에서 아래 코드 작성

  ```python
  def comment_create(request, board_id):
      # 댓글 생성하는 로직
      content = request.POST.get('content')
      comments = Comment(board_id=board_id, content=content)
      comments.save()
      return redirect('boards:detail', board_id)
  ```

- `boards/templates/boards/detail.html` 에서 댓글 작성부분 만들기

  ```html
  <form action="{% url 'boards:comment_create' board.id %}" method="post">
  	{% csrf_token %}
  	<input type="text" name="content"
             placeholder="댓글을 입력해주세요..."/>
  	<input type="submit" value="SUBMIT">
      </form>
  ```

  

## Comment 목록 보여주기

- `boards/views.py` 의 detail 함수 안에 아래 코드 추가

  ```pythjon
      comments = board.comment_set.order_by('-id').all()
      context = {'board': board, 'comments': comments}
  ```

- `boards/templates/boards/detail.html` 에서 댓글 보여주는 부분 추가

  ```html
  <p>
  	<b>Comments</b>
  </p>
  {% for comment in comments %}
  	<li>{{ comment.content }}</li>
  {% empty %}
  	<p class="text-info">첫번째 댓글을 달아주세요!</p>
  {% endfor %}
  ```

  

## Comment 삭제 url 작성

- `boards/urls.py` 의 urlpatterns 리스트에 아래 코드 추가

  ```python
  path('<int:board_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
  ```

- `board/views.py` 에 아래 코드 추가

  ```python
  @require_http_methods(['POST'])
  def comment_delete(request, board_id, comment_id):
      comment = get_object_or_404(Comment, id=comment_id)
      comment.delete()
      return redirect('boards:detail', board_id)
  ```

- `boards/templates/boards/detail.html` 댓글 보이는 부분을 수정

  ```html
  {% for comment in comments %}
  	<li>
  		<form action="{% url 'boards:comment_delete' board_id=board.id comment_id=comment.id %}"
  			  method="post">
  			{% csrf_token %}
  			{{ comment.content }}
  			<input type="submit" value="delete">
  		</form>
  	</li>
  {% empty %}
  	<p class="text-info">첫번째 댓글을 달아주세요!</p>
  {% endfor %}
  ```

  

