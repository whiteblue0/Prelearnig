# Git repository for 2 folder

### ★github의 repository가 init 폴더가 된다.

초기설정

1. ```git config --global user.name "HyeonSoo"```
   ```git config --global user.email "21port@naver.com"```
   유저 등록

   

2. ```git init "foldername"```

   폴더를 git 저장소로 설정

3. ```git remote add origin https://github.com/whiteblue0/repositoryname```
   git 폴더와 repository 연결

서로 다른 컴퓨터의 폴더 연결

※정확히는 github의 repository를 cloning하여 관리한다.

1. ```git clone https://github.com/whiteblue0/repositoryname```
   git init 하지 않은  다른 컴퓨터에 repository의 clone 폴더 생성
2. 생성한 폴더에 파일 생성 => git에 untracked 상태로 있음
3. ```git add .```
   untracked 상태인 파일들을 git에 add
4. ```git commit -m "message"```
   add한 파일에 commit으로 업로드시 코멘트 작성
5. ```git push```
   github로 업로드, 동기화 됨
6. 다른컴퓨터에서 사용할때
   - ```git pull``` 로 github의 파일을 local git 폴더와 동기화
   - 작업 완료 후 ```git add``` => ```git commit``` => ```git push``` 
     흐름순으로 다시 github와 동기화