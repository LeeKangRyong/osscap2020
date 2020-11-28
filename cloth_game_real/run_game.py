from matrix import *
import LED_display as LMD
import threading

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
		for x in range(m.get_dx()):
			if array[y][x] == 0:
				LMD.set_pixel(y, x, 0)
			elif array[y][x] == 1:
				LMD.set_pixel(y, x, 1)		
			elif array[y][x] == 2:
				LMD.set_pixel(y, x, 2)
			elif array[y][x] == 3:
				LMD.set_pixel(y, x, 3)		
			elif array[y][x] == 4:
				LMD.set_pixrel(y, x, 4)
			elif array[y][x] == 5:
				LMD.set_pixel(y, x, 5)		
			elif array[y][x] == 6:
				LMD.set_pixel(y, x, 6)	
			elif array[y][x] == 7:
				LMD.set_pixel(y, x, 7)		
			else:
				continue
			
			
#옷 입힌 상태의 배열 리턴
def wear_array(arr_final, arr_cloth):
	for i in range(32):
		for j in range(16):
			if ( arr_cloth[i][j] != 0):
				arr_final[i][j] = arr_cloth[i][j]
	return arr_final

##########함수들 끝

##########실제 실행 코드
LED_init()

### 시간 제어 코딩


### 퀴즈 코딩(명언)


### 옷입히기 코딩

# 캐릭터 미피 생성, chr 외에 나머지 모두 빈 배열
chr_miffy = Character(arr_final, arr_character, arr_final, arr_final, arr_final, arr_final)
chr_miffy.wear_arr()
oScreen= Matrix(chr_miffy.arr_final)


while True:
	key = input('Enter key')
	if key == 'r': #캐릭터 재생성
		#아마도 arr_final 초기화 시켜야 할듯 나중에 보고 추가
		chr_miffy = Character(arr_final, arr_character, arr_final, arr_final, arr_final, arr_final)
		
	elif key == 't':   #상의 선택 

	elif key == 'b':

	elif key == 's':
	
	elif key == '1':

	else:
		continue

	draw_matrix(oScreen)


class Character:
	def __init__(self, arr_final, arr_character, arr_top, arr_bottom, arr_shoes, arr_acc1, arr_acc2, arr_acc3):
	self.arr_final = arr_final
	self.arr_character = arr_character
	self.arr_top = arr_top
	self.arr_bottom = arr_bottom
	self.arr_shoes = arr_shoes
	self.arr_acc1 = arr_acc1
	self.arr_acc2 = arr_acc2
	self.arr_acc3 = arr_acc3

#출력 배열 바꾸기
	def wear_arr(self):
		for i in range(32):
			for j in range(16):
				if (self.arr_character[i][j] != 0 ):
					self.arr_final[i][j] = arr_character[i][j]
					
				if (self.arr_shoes[i][j] != 0 ):
					self.arr_final[i][j] = arr_shoes[i][j]
				
				if (self.arr_bottom[i][j] != 0 ):
					self.arr_final[i][j] = arr_bottom[i][j]
				
				if (self.arr_top[i][j] != 0 ):
					self.arr_final[i][j] = arr_top[i][j]
				
				if (self.arr_acc1[i][j] != 0 ):
					self.arr_final[i][j] = arr_acc1[i][j]
				
				if (self.arr_acc2[i][j] != 0 ):
					self.arr_final[i][j] = arr_acc2[i][j]
				
				if (self.arr_acc3[i][j] != 0 ):
					self.arr_final[i][j] = arr_acc3[i][j]
# 옷 결정 후 옷 정보  객체에 넣어주기
	def set_top(self, arr_top):
		self.arr_top = arr_top
	
	def set_bottom(self, arr_bottom):
		self.arr_bottom = arr_bottom
	
	def set_shoes(self, arr_shoes):
		self.arr_shoes = arr_shoes
	
	def set_acc1(self, arr_acc1):
		self.arr_acc1 = arr_acc1
	
	def set_acc2(self, arr_acc2):
		self.arr_acc2 = arr_acc2
	
	def set_acc3(self, arr_acc3):
		self.arr_acc3 = arr_acc3


#옷 선택하는 while







