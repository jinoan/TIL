# Anaconda 기본 명령어

> 참고: 
>
> - https://teddylee777.github.io/python/anaconda-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95-%ED%8C%81-%EA%B0%95%EC%A2%8C
>
> - https://medium.com/@5eo1ab/jupyter-notebook%EC%97%90-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-kernel-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0-ed5261a7e0e6

## 패키지 관련

### 설치된 패키지 목록 보기

```bash
$ conda list
```



### 패키지 설치

```bash
$ conda install pandas
```

```bash
$ conda install pandas numpy tensorflow
```



### 패키지 업데이트

```bash
$ conda update pandas
```



### 패키지 모두 업그레이드

```bash
$ conda upgrade --all
```



### 패키지 제거

```bash
$ conda remove pandas
```



### 설치된 패키지 검색

검색하고자 하는 키워드 양옆에 *를 씌우고 ''로 묶어서 검색

```bash
$ conda search '*pandas*'
```



## 가상환경 만들기

### 가상환경 생성

'my_python_env' 이름을 갖는 가상환경을 생성하고 싶으면

```bash
$ conda create -n my_python_env
```

패키지 install도 같이 하고 싶으면

```bash
$ conda create -n my_python_env pandas tensorflow
```

python 버전을 지정하고 싶으면

```bash
$ conda create -n my_python_env python=3.7
```



### 가상환경 시작 / 종료

'my_python_env' 가상환경 시작

```bash
$ conda activate my_python_env
```

가상환경 종료

```bash
$ conda deactivate
```



### 가상환경 .yaml 파일로 저장

```bash
$ conda env export > my_python_env.yaml
```



### .yaml 파일로 새로운 가상환경 만들기

```bash
$ conda env create -f my_python_env.yaml
```



### 가상환경 리스트 출력

```bash
$ conda env list
```



### 가상환경 제거

```bash
$ conda env remove -n my_python_env
```



## jupyter notebook, nb_conda, ipykernel

### jupyter notebook 설치

```bash
$ conda install jupyter notebook
```



### nb_conda 설치

```bash
$ conda install nb_conda
```

nb_conda가 설치되면 jupyter notebook 상단 탭에 conda 탭이 생성

conda 탭에서 개별 패키지 관리가 가능



### ipykernel 설치

```bash
$ pip install ipykernel
```



### jupyter notebook에 가상환경 kernel 추가

```bash
$ python -m ipykernel install --user --name my_python_env --display-name "[displayKenrelName]"
```

