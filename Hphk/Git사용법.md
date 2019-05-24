# Git
## 기본명령어
1. git 저장소 (repository) 초기화

   ```bash
   $ git init
   ```

   - 원하는 폴더를 저장소로 만들게 되면, `git bash` 에서는 `(master)` 라고 표기된다.
   - 그리고 숨김폴더로 `.git/` 이 생성된다.

2. 커밋할 목록에 담기 (Staging Area)

   ```bash
   $ git add .
   ```

   - 현재 작업 공간(Working Directory / Tree) 의 변경사항을 커밋할 목록에 추가한다. ( `add` )
   - `.` 리눅스에서 현재 디렉토리(폴더)를 표기하는 방법으로, 현재 내 폴더에 있는 파일의 변경사항을 전부 추가한다.
   - 단일파일만 추가하려면 `git add "파일이름"`
   - 폴더를 추가하려면 `git add "폴더이름/"`

3. 커밋하기

   ```bash
   $ git commit -m '_____'
   ```

   - 커밋을 할때에는 해당하는 버전의 이력을 의미하는 메세지를 반드시 적어준다.
   - 메세지는 지금 버전을 쉽게 이해할 수 있도록 작성한다.
   - 커밋은 현재 코드의 상태를 스냅샷 찍는 것이다.

4. 로그 확인하기

   ```bash
   $ git log
   commit a94c46d614ecab1a7cd17b9528a5ecb675ed2c82 (HEAD -> master)
   Author: Jinho Ahn <winarc24@gmail.com>
   Date:   Fri May 24 10:44:49 2019 +0900
   
       2019-05-24
   
   ```

   - 현재까지 커밋된 이력을 모두 확인할 수 있다.

5. git 상태 확인하기

   ```bash
   $ git status
   ```

   - CLI(Command Line Interface) 현재 상태를 알기 위해 반드시 명령어를 통해 확인한다.
   - 커밋할 목록에 담겨 있는지, untracked인지, 커밋할 내역이 있는지 등등 다양한 정보를 알려준다.