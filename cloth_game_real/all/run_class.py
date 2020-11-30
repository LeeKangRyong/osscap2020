
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
					self.arr_final[i][j] = self.arr_character[i][j]
					
				if (self.arr_shoes[i][j] != 0 ):
					self.arr_final[i][j] = self.arr_shoes[i][j]
				
				if (self.arr_bottom[i][j] != 0 ):
					self.arr_final[i][j] = self.arr_bottom[i][j]
				
				if (self.arr_top[i][j] != 0 ):
					self.arr_final[i][j] = self.arr_top[i][j]
				
				if (self.arr_acc1[i][j] != 0 ):
					self.arr_final[i][j] = self.arr_acc1[i][j]
				
				if (self.arr_acc2[i][j] != 0 ):
					self.arr_final[i][j] = self.arr_acc2[i][j]
				
				if (self.arr_acc3[i][j] != 0 ):
					self.arr_final[i][j] = self.arr_acc3[i][j]
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
