# Django 게시판 만들기 (3)



## 이미지 추가

- `boards/models.py` 에서 Board 클래스에 image 필드 추가

  ```python
  image = models.ImageField(blank=True)  # 해당 필드에 아무것도 안들어가도 된다.
  ```

- terminal에서 pillow 인스톨

  ```bash
  $ pip install pillow
  ```

- migration

  ```bash
  $ python manage.py makemigrations
  ```

  ```bash
  $ python manage.py migrate
  ```

- `boards/views.py` 에서 image를 받는 부분 추가

  ```python
  @require_http_methods(['GET', 'POST'])
  def new(request):
      # GET
      if request.method == 'GET':
          return render(request, 'boards/new.html')
      # POST
      else:
          title = request.POST.get('title')
          content = request.POST.get('content')
          image = request.FILES.get('image')  # <-
          board = Board(title=title, content=content, image=image)  # <-
          board.save()
          print('new board id: ', board.id)
          return redirect('boards:detail', board.id)
  ```

- `boards/templates/boards/new.html` 에 이미지 넣는 부분 추가

  ```html
      <form action="{% url 'boards:new' %}" method="post"
            enctype="multipart/form-data"> <!-- 여기 -->
          {% csrf_token %}  <!-- csrf 토큰을 함께 보낸다 -->
          <label for="title">Title</label><br />
          <input id="title" type="text" name="title"><br />
          <label for="content">Content</label><br />
          <textarea name="content" id="content"></textarea><br />
          <input type="file" name="image"
                 accept="image/*"/> <!-- 여기 --> <br /> 
          <input type="submit" />
      </form>
  ```

- `crud/settings.py` 에 이미지 저장경로 추가

  ```python
  # domain.com/media/sample.jpg
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  ```

- `crud/urls.py` 에 추가

  ```python
  from django.conf import settings
  from django.conf.urls.static import static
  
  # domain.com/media/sample.jpg
  urlpatterns += static(
      settings.MEDIA_URL,
      document_root=settings.MEDIA_ROOT
  )
  ```

- `boards/templates/boards/detail.html` 이미지 보이는 부분 추가

  ```bash
  {% if board.image %}
  <img src="{{ board.image.url }}" alt="{{ board.image.name }}">
  {% else %}
  <p> There is no image </p>
  {% endif %}
  <p>{{ board.content }}</p>
  ```

  

- `boards/templates/boards/edit.html` 수정

  ```html
      <form action="{% url 'boards:edit' board.id %}" method="post"
            enctype="multipart/form-data"> <!-- 여기 -->
          {% csrf_token %}  <!-- csrf 토큰을 함께 보낸다 -->
          <label for="title">Title</label><br />
          <input id="title" type="text" name="title" value="{{board.title}}"><br />
          <label for="content">Content</label><br />
          <textarea name="content" id="content">
              {{board.content}}
          </textarea><br />
          <input type="file" name="image"
                 accept="image/*"> <!-- 여기 --> <br />
          <input type="submit">
      </form>
  ```

- `boards/views.py` 에서 edit 함수에 image를 받는 부분 추가

  ```python
  # POST
  else:
      title = request.POST.get('title')
      content = request.POST.get('content')
      image = request.FILES.get('image')  # <-
      board.title = title
      board.content = content
      board.image = image  # <-
      board.save()
      return redirect('boards:detail', board_id)
  ```

  

## Django imagekit 활용

- pilkit 설치

  ```bash
  $ pip install pilkit
  ```

- django-imagekit 설치

  ```bash
  $ pip install django-imagekit
  ```

- `crud/settings.py` 안의  `INSTALLED_APPS` 리스트에 추가

  ```python
  # 3rd party Apps
  'imagekit',
  ```

- `boards/models.py` 에 추가 및 image field 수정

  ```python
  from imagekit.models import ProcessedImageField
  from imagekit.processors import Thumbnail
  ```

  ```python
  # image = models.ImageField(blank=True)  # 해당 필드에 아무것도 안들어가도 된다.
  image = ProcessedImageField(
  	processors=[Thumbnail(200, 300)]  # Thumbnail 형태로 200 * 300
  	format='JPEG',
      options={'quality': 90},  # 기존 퀄리티의 90% 정도로 설정
  )
  ```

- migration

  ```bash
  $ python manage.py makemigrations
  ```

  ```bash
  $ python manage.py migrate
  ```

- ProcessedImageField 에 나오는 설정들은 수정이 필요하더라도 수정 후 migration을 다시 할 필요가 없다.