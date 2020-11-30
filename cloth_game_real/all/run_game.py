from matrix import *
import LED_display as LMD
import threading
from top_all import *
from bot_all import *
from character import *
from naked import *
from run_class import *
from acc_all import *
from shoes_all import *

# LED 사용하기 위해 한번 실행
def LED_init():
	thread=threading.Thread(target=LMD.main, args=())
	thread.setDaemon(True)
	thread.start()
	return

# 배열의 숫자를 받아 매트릭스에 출력
def draw_matrix(oScreen):
	array = oScreen.get_array()
	for y in range(oScreen.get_dy()):
		for x in range(oScreen.get_dx()):
			if array[y][x] == 0:
				LMD.set_pixel(y, x, 0)
			elif array[y][x] == 1:
				LMD.set_pixel(y, x, 1)		
			elif array[y][x] == 2:
				LMD.set_pixel(y, x, 2)
			elif array[y][x] == 3:
				LMD.set_pixel(y, x, 3)		
			elif array[y][x] == 4:
				LMD.set_pixel(y, x, 4)
			elif array[y][x] == 5:
				LMD.set_pixel(y, x, 5)		
			elif array[y][x] == 6:
				LMD.set_pixel(y, x, 6)	
			elif array[y][x] == 7:
				LMD.set_pixel(y, x, 7)		
			else:
				continue
#배열 초기화 함수
def refresh_arr(arr):
	for y in range(32):
		for x in range(16):
			arr[y][x] = 0
	return arr
# 배열의 좌우 바꾸는 함수
def arr_converse(arr):
	conv_arr = []
	for j in range(-1,-17,-1):
		conv_arr.append(arr[j])
	return conv_arr
			

			
#옷 입힌 상태의 배열 리턴
##########함수들 끝

##########실제 실행 코드
LED_init()

### 시간 제어 코딩


### 퀴즈 코딩(명언)


### 옷입히기 코딩

# 캐릭터 미피 생성, chr 외에 나머지 모두 빈 배열
chr_miffy = Character(arr_final, arr_character, arr_final, arr_final, arr_final, arr_final, arr_final, arr_final)
chr_miffy.wear_arr()
oScreen= Matrix(chr_miffy.arr_final)

gameover =0
while True:
	draw_matrix(oScreen)
	key = input('Enter key')

	if key == 'r': #캐릭터 재생성
		arr_final = refresh_arr(arr_final)
		chr_miffy = Character(arr_final, arr_character, arr_final, arr_final, arr_final, arr_final, arr_final, arr_final)
		chr_miffy.wear_arr()
		oScreen = Matrix(chr_miffy.arr_final)
	elif key == 't':	#상의 선택 			
		chr_miffy.arr_top = refresh_arr(chr_miffy.arr_top)
		i = 0
		last = len(list_top)
		oScreen = Matrix(list_top[i])	
		while True:	
			draw_matrix(oScreen)
			key = input('Enter key')
			if key == 'd':
				if i == last -1:
					i = 0
				else:
					i = i+1
				oScreen = Matrix(list_top[i])
			elif key == 'a':
				if i == 0:
					i = last - 1
				else:
					i = i-1
				oScreen = Matrix(list_top[i])
			elif key == 'y': #옷 선택
				chr_miffy.arr_final = refresh_arr(chr_miffy.arr_final)
				chr_miffy.set_top(list_top[i])
				chr_miffy.wear_arr()
				oScreen = Matrix(chr_miffy.arr_final)
				break
			else:
				continue      #상의 선택 끝
		
	elif key == 'b':
		chr_miffy.arr_bottom = refresh_arr(chr_miffy.arr_bottom)
		i = 0
		last = len(list_bottom)
		oScreen = Matrix(list_bottom[i])
		while True:	
			draw_matrix(oScreen)
			key = input('Enter key')
			if key == 'd':
				if i == last - 1:
					i = 0
				else:
					i = i+1
				oScreen = Matrix(list_bottom[i])
			elif key == 'a':
				if i == 0:
					i = last - 1
				else:
					i = i-1
				oScreen = Matrix(list_bottom[i])
			elif key == 'y': #옷 선택
				chr_miffy.arr_final = refresh_arr(chr_miffy.arr_final)
				chr_miffy.set_bottom(list_bottom[i])
				chr_miffy.wear_arr()
				oScreen = Matrix(chr_miffy.arr_final)

				break
			else:
				continue      #하의 선택 끝
		
	elif key == 's':
		chr_miffy.arr_shoes = refresh_arr(chr_miffy.arr_shoes)
		i = 0
		last = len(list_shoes)
		oScreen = Matrix(list_shoes[i])
		while True:	
			draw_matrix(oScreen)
			key = input('Enter key')
			if key == 'd':
				if i == last -1:
					i = 0
				else:
					i = i+1
				oScreen = Matrix(list_shoes[i])
			elif key == 'a':
				if i == 0:
					i = last - 1
				else:
					i = i-1
				oScreen = Matrix(list_shoes[i])
			elif key == 'y': #옷 선택
				chr_miffy.arr_final = refresh_arr(chr_miffy.arr_final)
				chr_miffy.set_shoes(list_shoes[i])
				chr_miffy.wear_arr()
				oScreen = Matrix(chr_miffy.arr_final)
				break

			else:
				continue      #신발 선택 끝
		

# 1번 키는 악세사리 1 선택하는 거 
	elif key == '1':
		chr_miffy.arr_acc1 = refresh_arr(chr_miffy.arr_acc1)
		i = 0
		last = len(list_acc)
		oScreen = Matrix(list_acc[i])
		while True:	
			draw_matrix(oScreen)
			key = input('Enter key')
			if key == 'd':
				if i == last -1:
					i = 0
				else:
					i = i+1
				oScreen = Matrix(list_acc[i])
			elif key == 'a':
				if i == 0:
					i = last - 1
				else:
					i = i-1
				oScreen = Matrix(list_acc[i])
			elif key == 'y': #옷 선택
				chr_miffy.arr_final = refresh_arr(chr_miffy.arr_final)
				chr_miffy.set_acc1(list_acc[i])
				chr_miffy.wear_arr()
				oScreen = Matrix(chr_miffy.arr_final)
				break
			elif key == 'w':
				for x in range(32):
					list_acc[i][x] = arr_converse(list_acc[i][x])
					oScreen = Matrix(list_acc[i])
			else:
				continue      #신발 선택 끝
		

	elif key == '2':
		chr_miffy.arr_acc2 = refresh_arr(chr_miffy.arr_acc2)
		i = 0
		last = len(list_acc)
		oScreen = Matrix(list_acc[i])
		while True:	
			draw_matrix(oScreen)
			key = input('Enter key')
			if key == 'd':
				if i == last -1:
					i = 0
				else:
					i = i+1
				oScreen = Matrix(list_acc[i])
			elif key == 'a':
				if i == 0:
					i = last - 1
				else:
					i = i-1
				oScreen = Matrix(list_acc[i])
			elif key == 'y': #옷 선택
				chr_miffy.arr_final = refresh_arr(chr_miffy.arr_final)
				chr_miffy.set_acc2(list_acc[i])
				chr_miffy.wear_arr()
				oScreen = Matrix(chr_miffy.arr_final)
				break

			else:
				continue      #신발 선택 끝
		

	elif key == '3':
		chr_miffy.arr_acc3 = refresh_arr(chr_miffy.arr_acc3)
		i = 0
		last = len(list_acc)
		oScreen = Matrix(list_acc[i])
		while True:	
			draw_matrix(oScreen)
			key = input('Enter key')
			if key == 'd':
				if i == last -1:
					i = 0
				else:
					i = i+1
				oScreen = Matrix(list_acc[i])
			elif key == 'a':
				if i == 0:
					i = last - 1
				else:
					i = i-1
				oScreen = Matrix(list_acc[i])
			elif key == 'y': #옷 선택
				chr_miffy.arr_final = refresh_arr(chr_miffy.arr_final)
				chr_miffy.set_acc3(list_acc[i])
				chr_miffy.wear_arr()
				oScreen = Matrix(chr_miffy.arr_final)
				break

			else:
				continue      #신발 선택 끝
		















	if(key == 'q'):
		break
#시간제어 변수로 종료 제어
	
