# Wanted pre_task

## Skills
### Language
- [Python](https://github.com/python)
### Framework
- [FastAPI](https://github.com/fastapi/fastapi)
### RDB
- [MySQL](https://github.com/mysql)
### ORM
- [Tortoise ORM](https://github.com/tortoise/tortoise-orm)

## 구현 기능
- 회사명 자동완성
- 회사 이름으로 회사 검색
- 새로운 회사 추가

## DB Diagram
![image](https://github.com/user-attachments/assets/3c366a83-5670-4064-a770-78486493aef5)

## 체크 리스트
- [x] API가 정상 작동 하는가
- [x] 유닛테스트는 작성 되었는가

## env
- local_env.sh
  - API_ENV = "local"
  - DB_URL = 로컬 DB 주소
 
- test_env.sh
  - API_ENV = "test"
  - DB_URL = 로컬 DB 주소
  - TEST_DB_URL = 테스트 DB 주소
