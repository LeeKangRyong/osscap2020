가 4팀 프로젝트 사용 방법


1. sudo apt-get install python3-bs4  (날씨 불러오기 위한 bs4 라이브러리)

2. sudo apt-get install python3-requsets(sudo apt-get install python-requsets (날씨 불러오기 위한 requests 설치)

rpi-rgb-led-matrix/bindings/python/       이 경로에서 아래 3,4,5번 명령어를 실행(rgb-matrix 라이브러리 사용을 위한 환경 설정) 
 https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python 참고

3. sudo apt-get update && sudo apt-get install python3-dev python3-pillow -y  

4. make build-python PYTHON=$(which python3)

5. sudo make install-python PYTHON=$(which python3)


6. (텍스트 출력때 사운드 관련 오류가 뜬다면) /etc/modprobe.d/raspi-blacklist.conf  에 blacklist snd_bcm2835 추가
    만약 raspi-blacklist.conf 가 없다면 vi raspi-blacklist.conf 를 vi 로 만든 뒤  blacklist snd_bcm2835 추가

7. 네이버 초록창에 '날씨' 를 검색 후 그 주소를  html =  requests.get(" ") 의 따옴표 사이에 입력

8. osscap2020/cloth_game_rael/ final/all / run_game_test.py 실행 ( python3 run_game_test.py)  >>옷입히기 게임
시간 입력(초단위) 뒤 't' : 상의 선택 화면,  'b: 바지선택화면,  's' 신발 선택화면, '1','2',3' 악세서리 선택 화면
'y' : 옷 선택
'r': 리셋 
't' 'b' 's' '1' '2' '3' 재입력시 해당 부분 재선택

9. osscap2020/cloth_game_rael/ final/all / quiz_real.py 실행 (sudo python3 quiz_real.py)   >>텍스트(문제) 출력




###원래는 텍스트 출력과 옷입히기 게임을 합쳐야 했지만 합치지 못했습니다.

데모 영상 유투브 링크!
https://www.youtube.com/watch?v=LqZHLqER6Io
