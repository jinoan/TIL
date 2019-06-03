# MTV pattern

- Model
- Template (MVC 패턴의 view에 해당)
- View (MVC 패턴의 Controller 에 해당)



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
   ```

3. `./pages/templates/index.html`

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

4. `./pages/templates/dinner.html`

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

5. `./pages/templates/greeting.htnl`

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

    

