# 08_pjt

## 회고 - 방성준
- **Liked (좋았던 점)**
    - Ajax의 Django 사용법을 차분히 익히고 익숙해져 나가는 시간이 돼서 좋았다.
    - Git branch 전략 수립을 잘했다. 충돌을 최소화하고 충돌이 발생해도 차분하게 페어와 함께 풀어나갔다.

- **Learned (배운 점)**
    - Ajax를 활용한 클라이언트 서버 간 동작 방식을 이해했다.
        - XHR 객체 생성 및 요청 -> Ajax 요청 처리 -> 응답 데이터 생성 -> JSON 데이터 응답 -> Promise 객체 데이터를 활용해 DOM 조작 (웹 페이지의 일부분만을 다시 로딩)
    - 협업하는 법에 익숙해졌다.
        - Git branch 전략을 배웠다. 
            - test branch
                - movies branch
                - accounts branch
                - community branch
            - 앱별로 브랜치를 나누었으며 충돌에 대비해 test 브랜치에서 병합을 진행하고 최종 테스트를 수행해봤는데 성공적이였다.
        - 기능별로 역할을 나누어 과제를 수행했는데, 생각보다 훨씬 효율적이였던 것 같다. 이후 프로젝트에서의 역할 분배 방법론을 익힌 것 같다.

- **Lacked (부족했던 점)**
    - Ajax가 Django에서 어떤 형식으로 데이터를 주고 받는지 이해가 부족했던 것 같다. 프로젝트 수행 시간의 대부분을 이러한 점을 채우고 공부하는데 사용했다.
    - 시간이 넉넉하다 생각했으나 시간이 부족했다. 이후의 프로젝트에선 일정 관리에 신경을 써야할 것 같다.


- **Longed for (바람직했던 점)**
    - 원활한 의사소통
        - 페어와 의사소통이 원활했다. 역할 분배부터 코드 리뷰까지 원활하고 즐거운 분위기에서 개발할 수 있었다.
        - 막히는 부분이 있으면 서로 도움을 즉각적으로 줄 수 있어 좋았다. 이러한 분위기를 앞으로도 유지해 나가야겠다.
    - 프로젝트를 통한 성장
        - 스스로에게 부족했던 부분을 프로젝트를 통해 알 수 있었다.
        - 구현했다고 단순히 만족하는 것이 아닌 확실하게 이해할 때까지 페어와 코드 리뷰를 하며 성장할 수 있었다.



## 회고 - 이승주
- **Liked (좋았던 점)**
    - 기능별로 파트를 분배하여, 각 기능을 백엔드와 프론트엔드 관점에서 바라보며 복습할 수 있는 시간을 가질 수 있었다.

- **Learned (배운 점)**
    1. **Python 인터프리터 설정**
        - `requirements.txt`로 패키지를 설치한 후에도 Python 경로를 인식하지 못해 오류가 발생.
            - 가상환경을 설정하면, 해당 환경만을 위한 ****Python 인터프리터가 venv 폴더에 설치
            - 가상환경의 인터프리터 경로를 직접 설정해야 함
            - venv - Scripts - python 경로 선택
        
    2. **Git 브랜치 관리**
        - test라는 브랜치로 작업을 진행하고 github에 push 한 후, 다른 환경에서 이 작업물을 받아오고 싶다면
            - github의 master 브랜치에서 초기 파일을 클론 받은 후, test 브랜치를 새로 생성하고 switch하여 `git pull origin test` 로 test 브랜치에서 작업한 내용을 로컬로 가져오기
        - **브랜치 병합 (merge)**
            - 특정 브랜치에서 다른 로컬 브랜치를 병합할 때 ( test 브랜치에 movies라는 로컬 브랜치를 병합하려면 `test` 브랜치로 이동(switch)한 후, merge 명령.
            - 원격 레포에서 받아오고 싶으면 git pull origin 원격레포.
            

- **Lacked (부족했던 점)**
    - 이벤트 발생 시 js에서 value를 axios로 전달하고 이를 django view에서 처리하는 방식에 대한 이해가 부족하여 시간이 오래 걸림.
        - value 값을 js의 data 객체에 담아 axios로 django에 보내고, django view에서 처리할 때는
        - `body = json.loads(request.body)` `genre_name = body.get('genre')`로 데이터 받아 와서 처리 가능


- **Longed for (바람직했던 점)**

    - 프로젝트 초반부터 Git 관리 전략을 세우고, VS Code와 GitHub에서 병합하는 방법을 익히며 체계적으로 프로젝트를 관리함. 기능 별로 branch를 관리하고 나중에 merge하는 방식으로 프로젝트를 체계적으로 관리하고 있다는 느낌을 받았음.