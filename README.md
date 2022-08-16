# django-blog

### blog 제작 - bookmark/blog/album/login 기능 구현 및 폼 변경/삭제/생성 기능 구현

---
<br>

### 1.가상환경 설치 및 필요 패키지 설치

```
> python -m venv env
> ./env/Scripts/activate  # 가상환경 접속 (window)
> source env/bin/activate # 가상환경 접속 (ubuntu)

> (env) pip install -r requirements.txt
```

### 2.runserver 실행하기

> mange.py 파일이 존재하는 위치에서 runserver를 열어야 한다.

```
> (env) python manage.py runserver [port 번호]
```

<br>

> local 환경에서는 127.0.0.1로 접속하면 구현된 blog 웹사이트를 테스트 할 수 있다.