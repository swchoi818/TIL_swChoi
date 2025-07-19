# git 기초 문법
- touch 파일 생성
- mkdir 디렉토리 생성 
- ls 현재 작업 중인 디렉토리 내부의 폴더/파일 목록
- cd 현재 작업 중인 디렉토리를 변경 (위치 이동)
- start 폴더/파일 열기 (Mac 에서는 open 사용)
- rm 파일 삭제 (디렉토리 삭제는 -r)
- pwd 현재 작업 중인 폴더(디렉토리)의 절대 경로를 출력
--- 
# 경로
- / 루트 디렉토리 : 모든 주소의 시작점
- ~ 홈 디렉토리 : 터미널을 처음 켰을 때 시작하는 나의 기본 공간
- 절대 경로
 - 루트 부터 목적지까지의 전체 주소
 - 누가 어디서 보든 항상 똑같은 주소
 - 예시 : /User/ssafy/Desktop
- 상대 경로 
 - 현재 내 위치를 기준으로 한 주소
 - '옆방으로 가' (Desktop), '위 층으로 올라가'(..) 등 
---
# git의 영역
- Working Directroy : 실제 작업 중인 파일들이 위치하는 영역
- Staging Area : Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
- Repository : 버전 이력과 파일들이 영구적으로 저장되는 영역, 모든 버전과 변경 이력이 기록됨
- Commit : 변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록하여 smnpshot 이라고도 함
---
# git 동작
- git init : 로컬 저장소 설정
- git add : 변경사항이 있는 파일을 staging area에 추가
- git commit : staging area에 있는 파일들을 저장소에 기록
- git 사용자 정보 등록
 - git config --global user.email "메일주소"
 - git config --global user.name "사용자 이름"
- git status : 현재 로컬 저장소의 파일 상태 보기
- git log : commit history 보기
- git log --oneline : commit 목록 한 줄로 보기
- git config --global -l : git global 설정 정보 보기
---
# commit 수정하기
- git commit --amend : Commit 메시지 수정
---
# 원격 저장소 연결
- git remote add origin(repos 별명 지정) remote_repo_url(repos 주소) : 로컬 저장소에 원격 저장소 추가
- git push origin(repos 별명) master(branch 이름) : repos에 commit 목록 업로드
- git pull origin(repos 별명) master(branch 이름) : 원격 저장소의 변경사항만을 받아옴
- git clone remote_repo_url : 원격 저장소 전체를 복사
- gitignore : git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 텍스트 파일
- git remote -v : 현재 로컬 저장소에 등록된 원격 저장소 목록 보기
- git remote rm 원격 저장소 이름 : 현재 로컬 저장소에 등록된 원격 저장소 삭제
---
# Revert & Reset
- git revert <commit id> 
 - "재설정" 
 - 단일 commit을 실행 취소 하는 것
 - 프로젝트 기록에서 commit을 없었던 일로 처리 후 그 결과를 새로운 commit으로 추가함
- git reset [옵션] <commit id>
 - "되돌리기"
 - 시계를 마치 과거로 돌리는 듯한 행위
 - 특정 commit으로 되돌아 갔을 때, 되돌아간 commit 이후의 commit은 모두 삭제
 - --soft : 삭제된 commit의 기록을 staging area에 남김
 - --mixed : 삭제된 commit의 기록을 working directory에 남김
 - --hard : 삭제된 commit의 기록을 남기지 않음
---
- git restore : Working Directroy에서 파일을 수정한 뒤, 파일의 수정 사항을 취소하고, 원래 모습대로 되돌리는 작업
- git rm --cashed : Staging Area에서 Working Directory로 되돌리기(git 저장소에 commit이 없는 경우)
- git rm --cashed : Staging Area에서 Working Directory로 되돌리기(git 저장소에 commit이 없는 경우)
- git rm --staged : Staging Area에서 Working Directory로 되돌리기(git 저장소에 commit이 존재하는 경우)