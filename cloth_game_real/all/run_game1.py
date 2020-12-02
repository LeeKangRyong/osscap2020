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
import time
from copy import *
from recom_all import *
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
			if array[y][x] ==0:
				LMD.set_pixel(y, x, 0)
			elif array[y][x] == 1:
				LMD.set_pixel(y, x, 1)		
			elif array[y][x] == 2:
				LMD.set_pixel(y, x, 2)
			elif array[y][x] == 3:
				LMD.set_pixel(y, x, 3)		
			elif array[y][x]  == 4:
				LMD.set_pixel(y, x, 4)
			elif array[y][x] == 5:
				LMD.set_pixel(y, x, 5)		
			elif array[y][x] == 6:
				LMD.set_pixel(y, x, 6)	
			elif array[y][x] == 7:
				LMD.set_pixel(y, x, 7)
			elif array[y][x] == 9:
				LMD.set_pixel(y, x, 0)
			else:i
				continue
#배열 초기화 함수
def refresh_arr(arr):
	for y in range(32):
		for x in range(16):
			arr[y][x] = 0
	

#옷 추천 여부 판단
def recommend(arr_cloth, arr_recom, oScreen, temp):
    if (temp >= 20):
        if arr_cloth[31][15] == 10 :
            oScreen.paste(arr_recom[0], 0, 0)
        elif arr_cloth[31][15] == 20:
            oScreen.paste(arr_recom[1], 0, 0)
    elif (temp < 20):
        if arr_cloth[31][15] == 10:
            oScreen.paste(arr_recom[1], 0, 0)
        elif arr_cloth[31][15] == 20:
            oScreen.paste(arr_recom[0], 0, 0)
    return oScreen
    
    





'''
# 배열의 좌우 바꾸는 함수
def arr_converse(print_arr):
    conv_arr = [[0 for x in range(16)] for y in range(32)]
    for i in range(32):
	    for j in range(-1,-17,-1):
		    conv_arr[i][(-j-1)] = print_arr[i][j]
    print_arr = deepcopy(conv_arr)	
'''
			
def arr_converse(print_arr):
    conv_arr = deepcopy(print_arr)
    for i in range(32):
	    for j in range(-1,-17,-1):
		    conv_arr[i][(-j-1)] = print_arr[i][j]
    print_arr = deepcopy(conv_arr)
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
print_arr = []


def change_arr(print_arr):       #출력위치 바꾸는 함수
	check_arr = 0   
	for i in range(32):
		for j in range(16): 
			if( print_arr[i][j] != 0):
				x = 0
				while( i + x < 32 ):
					if i == 0:
						break
					print_arr[x] = print_arr[i+x]
					print_arr[i+x] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
					x += 1
				for n in range(20):
					print_arr[31-n] = print_arr[19-n] 
					print_arr[19-n] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


				check_arr = 1
				break
		if (check_arr == 1):
			break


while True:
	draw_matrix(oScreen)
	key = input('Enter key')

	if key == 'r': #캐릭터 재생성
		refresh_arr(arr_final)
		chr_miffy = Character(arr_final, arr_character, arr_final, arr_final, arr_final, arr_final, arr_final, arr_final)
		chr_miffy.wear_arr()
		oScreen = Matrix(chr_miffy.arr_final)

	elif key == 't':	#상의 선택 			
		refresh_arr(chr_miffy.arr_top)
		i = 0
		last = len(list_top)
		print_arr = deepcopy(list_top[i])
		change_arr(print_arr)
		oScreen = Matrix(print_arr)			

		while True:	
			draw_matrix(oScreen)
			key = input('Enter key')
			if key == 'd':
				if i == last -1:
					i = 0
				else:
					i = i+1
				print_arr = deepcopy(list_top[i])
				change_arr(print_arr)
				oScreen = Matrix(print_arr)			
                                
                                #추천 기능 
                                oSreen = recommend(list_top[i], arr_recom, oScreen, 10) 
				
			elif key == 'a':
				if i == 0:
					i = last - 1
				else:
					i = i-1 
				print_arr = deepcopy(list_top[i])
				change_arr(print_arr)
				oScreen = Matrix(print_arr)			
                                
                                #추천 기능 
                                oSreen = recommend(list_top[i], arr_recom, oScreen, 10) 

				
			elif key == 'y': #옷 선택
				refresh_arr(chr_miffy.arr_final)
				chr_miffy.set_top(deepcopy(list_top[i]))
				chr_miffy.wear_arr()
				oScreen = Matrix(chr_miffy.arr_final)
				break
			else:
				continue      #상의 선택 끝
				
	elif key == 'b':
		refresh_arr(chr_miffy.arr_bottom)
		i = 0
		last = len(list_bottom)
		print_arr = deepcopy(list_bottom[i])
		change_arr(print_arr)
		oScreen = Matrix(print_arr)			
		while True:	
			draw_matrix(oScreen)
			key = input('Enter key')
			if key == 'd':
				if i == last - 1:
					i = 0
				else:
					i = i+1
				print_arr = deepcopy(list_bottom[i])
				change_arr(print_arr)
				oScreen = Matrix(print_arr)			
			elif key == 'a':
				if i == 0:
					i = last - 1
				
				else:
					i = i-1
				print_arr = deepcopy(list_bottom[i])
				change_arr(print_arr)
				oScreen = Matrix(print_arr)			
			elif key == 'y': #옷 선택
				refresh_arr(chr_miffy.arr_final)
				chr_miffy.set_bottom(deepcopy(list_bottom[i]))
				chr_miffy.wear_arr()
				oScreen = Matrix(chr_miffy.arr_final)
				break
			else:
				continue      #하의 선택 끝
		
	elif key == 's':
		refresh_arr(chr_miffy.arr_shoes)
		i = 0
		last = len(list_shoes)
		print_arr = deepcopy(list_shoes[i])
		change_arr(print_arr)
		oScreen = Matrix(print_arr)			
		while True:	
			draw_matrix(oScreen)
			key = input('Enter key')
			if key == 'd':
				if i == last -1:
					i = 0
				else:
					i = i+1
				print_arr = deepcopy(list_shoes[i])
				change_arr(print_arr)
				oScreen = Matrix(print_arr)			
			elif key == 'a':
				if i == 0:
					i = last - 1
				else:
					i = i-1
				print_arr = deepcopy(list_shoes[i])
				change_arr(print_arr)
				oScreen = Matrix(print_arr)			
			elif key == 'y': #옷 선택
				refresh_arr(chr_miffy.arr_final)
				chr_miffy.set_shoes(deepcopy(list_shoes[i]))
				chr_miffy.wear_arr()
				oScreen = Matrix(chr_miffy.arr_final)
				break

			else:
				continue      #신발 선택 끝
		

# 1번 키는 악세사리 1 선택하는 거 
	elif key == '1':
		refresh_arr(chr_miffy.arr_acc1)
		i = 0
		last = len(list_acc)
		print_arr = deepcopy(list_acc[i])
		change_arr(print_arr)
		oScreen = Matrix(print_arr)			
		while True:	
			draw_matrix(oScreen)
			key = input('Enter key')
			if key == 'd':
				if i == last -1:
					i = 0
				else:
					i = i+1
				print_arr = deepcopy(list_acc[i])
				change_arr(print_arr)
				oScreen = Matrix(print_arr)			
			elif key == 'a':
				if i == 0:
					i = last - 1
				else:
					i = i-1
				print_arr = deepcopy(list_acc[i])
				change_arr(print_arr)
				oScreen = Matrix(print_arr)			
		
			elif key == 'y': #옷 선택
				refresh_arr(chr_miffy.arr_final)
				chr_miffy.set_acc1(deepcopy(list_acc[i]))
				chr_miffy.wear_arr()
				oScreen = Matrix(chr_miffy.arr_final)
				break
			elif key == 'w':
				arr_converse(print_arr)
				oScreen = Matrix(print_arr)
			else:
				continue      #신발 선택 끝
		

	elif key == '2':
		refresh_arr(chr_miffy.arr_acc2)
		i = 0
		last = len(list_acc)
		print_arr = deepcopy(list_acc[i])
		change_arr(print_arr)
		oScreen = Matrix(print_arr)			
		while True:	
			draw_matrix(oScreen)
			key = input('Enter key')
			if key == 'd':
				if i == last -1:
					i = 0
				else:
					i = i+1
				print_arr = deepcopy(list_acc[i])
				change_arr(print_arr)
				oScreen = Matrix(print_arr)			
			elif key == 'a':
				if i == 0:
					i = last - 1
				else:
					i = i-1
				print_arr = deepcopy(list_acc[i])
				change_arr(print_arr)
				oScreen = Matrix(print_arr)			
			elif key == 'y': #옷 선택
				refresh_arr(chr_miffy.arr_final)
				chr_miffy.set_acc2(deepcopy(list_acc[i]))
				chr_miffy.wear_arr()
				oScreen = Matrix(chr_miffy.arr_final)
				break
			elif key == 'w':
				arr_converse(print_arr)
				oScreen = Matrix(print_arr)
			else:
				continue      #신발 선택 끝
		

	elif key == '3':
		refresh_arr(chr_miffy.arr_acc3)
		i = 0
		last = len(list_acc)
		print_arr = deepcopy(list_acc[i])
		change_arr(print_arr)
		oScreen = Matrix(print_arr)			
		while True:	
			draw_matrix(oScreen)
			key = input('Enter key')
			if key == 'd':
				if i == last -1:
					i = 0
				else:
					i = i+1
				print_arr = deepcopy(list_acc[i])
				change_arr(print_arr)
				oScreen = Matrix(print_arr)			
			elif key == 'a':
				if i == 0:
					i = last - 1
				else:
					i = i-1
				print_arr = deepcopy(list_acc[i])
				change_arr(print_arr)
				oScreen = Matrix(print_arr)			
			elif key == 'y': #옷 선택
				refresh_arr(chr_miffy.arr_final)
				chr_miffy.set_acc3(deepcopy(list_acc[i]))
				chr_miffy.wear_arr()
				oScreen = Matrix(chr_miffy.arr_final)
				break

			elif key == 'w':
				arr_converse(print_arr)
				oScreen = Matrix(print_arr)
			else:
				continue      #신발 선택 끝
		





	if(key == 'q'):
		break
#시간제어 변수로 종료 제어
	
