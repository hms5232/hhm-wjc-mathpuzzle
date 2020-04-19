""" 
頻道切換 

有 100 個頻道，只能用前後/上下來切換頻道（可循環）。使用者現在輸入a、b兩個頻道，請問最短需要按幾次遙控器？
"""


while True:
	# 從 a 頻道切換到 b 頻道
	a = int(input())
	b = int(input())
	
	# 兩個都輸入 -1 的時候就停止
	if a == b == -1:
		break
	
	if abs(b - a) > 50:
		print(100 - abs(b - a))
	else:
		print(abs(b - a))