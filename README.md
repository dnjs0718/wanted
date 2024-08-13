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
### Containerization Platform
- [Docker-compose](https://github.com/docker/compose)

## 구현 기능
- 회사명 자동완성
- 회사 이름으로 회사 검색
- 새로운 회사 추가

## DB Diagram
![image](https://github.com/user-attachments/assets/3c366a83-5670-4064-a770-78486493aef5)

## 체크 리스트
- [x] API가 정상 작동 하는가
- [x] 유닛테스트는 작성 되었는가
- [x] 도커 환경을 만들었는가

## env
- local_env.sh
  ```script
  export API_ENV = "local"
  export DB_URL = 로컬 DB 주소
  ```
 
- test_env.sh
  ```script
  export API_ENV = "test"
  export DB_URL = 로컬 DB 주소
  export TEST_DB_URL = 테스트 DB 주소
  ```
- .env
  ```script
  DB_USER=디비 유저명
  DB_PASSWORD=디비 패스워드
  DB_URL=mysql://${DB_USER}:${DB_PASSWORD}@db/wanted?charset=utf8mb4
  API_ENV=local
  TEST_DB_URL=mysql://${DB_USER}:${DB_PASSWORD}@db/test_wanted?charset=utf8mb4
  ```

## Tips
- `wanted_data.sql` 덤프 파일을 만들어 놓았습니다. 목데이터가 필요할 시, 해당 SQL문을 임포트 할 수 있습니다!
