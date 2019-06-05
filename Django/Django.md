# MTV pattern

- Model

- Template (MVC 패턴의 view에 해당)

- View (MVC 패턴의 Controller 에 해당)

  

---

# Django

### Django 설치

```bash
$ pip install django
```



### Django project 생성

```bash
$ django-admin startproject intro .
```



### Django server 실행

```bash
$ python manage.py runserver
```



### Django app 생성

```bash
$ python manage.py startapp pages
```



### View 설정

1. `./intro/urls.py`
   
    ```python
    urlpatterns = [  # url을 모아놓는 리스트
        path('introduce/<str:name>/<int:age>', views.introduce),
        path('greeting/<str:name>/', views.greeting),  # greeint page의 url
        path('dinner/', views.dinner),  # dinner page의 url
        path('index/', views.index),  # index page의 url
        path('admin/', admin.site.urls),  # admin page의 url
    ]
    ```
    
    
    
2. `./pages/views.py`

   ```python
   def index(request):  # index url 요청 시 띄울 화면: index.html 파일
       return render(request, 'index.html')
   
   def dinner(request):  # dinner url 요청 시 띄울 화면: index.html 파일
       menu = ['순대국밥', '쌀국수', '햄버거', '곱창']
       choice = random.choice(menu)
       return render(request, 'dinner.html', {'dinner': choice})
   
   def greeting(request, name):
       return render(request, 'greeting.html', {'name': name})
   
   def introduce(request, name, age):
       return render(request, 'introduce.html', {'name': name, 'age': age})
   ```

   

3. html 파일 생성

    - `./pages/templates/index.html`

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>Title</title>
      </head>
      <body>
          <h1>Hello World!</h1>
      </body>
      </html>
      ```

      pages (django app) 폴더 안에 templates 폴더를 생성하고 그 안에 html 파일을 넣는다.

      

    - `./pages/templates/dinner.html`

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>Title</title>
      </head>
      <body>
          <h1>Dinner Page</h1>
          <p>오늘의 저녁 메뉴는 {{ dinner }} 입니다 ^0^/</p>
      </body>
      </html>
      ```

      

    - `./pages/templates/greeting.htnl`

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>Title</title>
      </head>
      <body>
          <h1>Hello {{name}}!</h1>
      </body>
      </html>
      ```

      

    - `./pages/templates/introduce.html`

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>Title</title>
      </head>
      <body>
          <h1>Introduce</h1>
          <p>{{name}} 님의 나이는 {{age}} 입니다.</p>
      </body>
      </html>
      ```

      

---

### Template Lenguage

1. 반복문

   ```html
   {% for menu in menus %}
   	<p>{{ menu }}</p>
   {% endfor %}
   <hr />
   
   {% for menu in menus %}
   	<p>{{ forloop.counter }} {{ menu }}</p> <!-- loop 횟수를 출력 -->
   {% endfor %}
   <hr />
   
   {% for user in empty_list %}
   	<p>{{ user }}</p>
   {% empty %}
   <!-- empty: for 태그 안에 optional 하게 있음, 빈 리스트일때 출력됨 -->
   	<p>현재 가입한 유저가 없습니다.</p>
   {% endfor %}
   ```

   

2. 조건문

   ```html
   {% if '짜장면' in menus %}
   	<p>짜장면에는 고추가루지!</p>
   {% endif %}
   <hr />
   
   {% for menu in menus %}
   	{{ forloop.counter }} 번째 도는중
   	{% if forloop.first %}
   		<p>짜장면 + 고추가루</p>
   	{% else %}
   		<p>{{ menu }}</p>
   	{% endif %}
   {% endfor %}
   ```

   

3. length filter 활용

   ```html
   {% for message in messages %}
   	{% if message|length > 5 %}  <!-- message의 길이(index)가 5보다 크면 -->
   		<p>메세지의 길이가 너무 길어요!</p>
   	{% else %}
   		<p>{{ message }} {{ message|length }}</p>
   	{% endif %}
   {% endfor %}
   ```

   

4. lorem ipsum

   ```html
   {% lorem %}
   <hr />
   {% lorem 3 w %}
   <hr />
   {% lorem 4 w random %}
   <hr />
   {% lorem 2 p %}
   ```

   - 의미없는 문장이나 단어로 테스트 용도로 웹페이지상에서 어떻게 보여지는지 확인하는 용도

     

5. 글자수 제한 (truncate)

   ```html
   <p>{{ my_sentence|truncatewords:3 }}</p> 단어 단위로 제한
   <p>{{ my_sentence|truncatechars:4 }}</p> 문자 단위로 제한
   <p>{{ my_sentence|truncatechars:10 }}</p> 띄어쓰기 포함
   ```

   

6. 글자 관련 필터

   ```html
   <p>{{ 'abc'|length }}</p>  <!-- 문자열 길이 -->
   <p>{{ 'ABC'|lower }}</p>  <!-- 모두 소문자로 -->
   <p>{{ 'abc'|upper }}</p>  <!-- 모두 대문자로 -->
   <p>{{ my_sentence|title }}</p>  <!-- 타이틀 형식으로 변경 (This Is Title) -->
   <p>{{ menus|random }}</p>  <!-- 리스트에서 랜덤으로 하나 출력 -->
   ```

   

7. 연산

   ```html
   <p>{{ 4|add:6 }}</p>  <!-- 덧셈 -->
   ```

   

8. 날짜표현

   ```html
   <p>{{ datetimenow }}</p>  <!-- views 파일에서 datetime을 불러올 수 있다 -->
   
   <!--
   	template lenguage에서는 now 키워드를 이용해
   	현재 날짜와 시간을 가져올 수 있다
   -->
   <P>{% now 'DATETIME_FORMAT' %}</P>  <!-- 2019년 6월 4일 5:34 오후 -->
   <P>{% now 'SHORT_DATETIME_FORMAT' %}</P>  <!-- 2019-6-4 17:34 -->
   <P>{% now 'DATE_FORMAT' %}</P>  <!-- 2019년 6월 4일 -->
   <P>{% now 'SHORT_DATE_FORMAT' %}</P>  <!-- 2019-6-4. -->
   <hr />
   
   <!-- 날짜 및 시간 따로 가져오기 -->
   {% now "Y년 m월 d일 (D) h:i" %}  <!-- 2019년 06월 04일 (화요일) 05:34 -->
   <hr />
   
   {% now "Y" as current_year %}  <!-- 현재 연도 값을 current_year로 선언 -->
   <p>Copyright {{current_year}}</p>  <!-- Copyright 2019 -->
   
   <!-- views.py에서 가져온 datetime의 형식 변경 -->
   {{ datetimenow|date:"SHORT_DATE_FORMAT" }}  <!-- 2019-6-4. -->
   <hr />
   ```

   

9. url 만들기

   ```html
   <p>{{ 'google.com'|urlize }}</p>
   ```

   

---

