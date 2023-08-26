# Firefighter

---

__실행 순서__
1. 사용자가 앱 실행하고 위치 정보를 소방서에 전송
2. 소방서는 전송받은 위치정보를 드론에 전송
3. 드론은 전송받은 위치로 이동
4. 위치로 이동한 드론은 화재위치로 정밀조정
5. 조정 완료한 드론은 소화기 투척
6. 미션 완료 후 제자리 복귀

![image](https://github.com/rhrnakrkawk/Project_Firefighting-Drone/assets/125804293/1e424066-bdb5-43ef-b1b1-6e79c3586325)

---

# Application

__첫 번째 화면__
- 지도로 현재 위치 표현
- 오른쪽 아래의 버튼으로 위치정보(위도, 경도) 저장
- 저장 후 다음 화면으로 이동

__두 번째 화면__
- 첫 번째 화면으로부터 받은 정보 출력
- 저장된 위치정보 전송
- MQTT 통신 프로토콜 사용

<img src = "https://github.com/rhrnakrkawk/Project_Firefighting-Drone/assets/125804293/9e411383-4e81-43bf-bf7c-b14d0be59ee1" width="25%" height="25% ">
<img src = "https://github.com/rhrnakrkawk/Project_Firefighting-Drone/assets/125804293/80735528-d988-4cf8-9b06-d9b0fc34e68c" width="25%" height="25% ">

# Firefighter_Drone
