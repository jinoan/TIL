# 리눅스 서버간 파일 복사 (scp)

> 참고: https://ngee.tistory.com/264

서버 1에서 서버 2로 파일을 복사한다고 가정

서버 1의 terminal에서 실행

`scp __복사하려는_파일_경로와_이름__ __id__@__ip_address__:__붙여넣기할_경로__`

```bash
$ scp ./test.txt test@192.168.0.30:/home/test
```



폴더를 복사하려는 경우 `-r` 옵션 추가

```bash
$ scp -r ./test_folder test@192.168.0.30:/home/test/dev
```