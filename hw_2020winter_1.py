'''
        ......  ......  ......
       7  14  28  56 112  ......
    3  6  12  24  48  96  ......
 1  2  4   8  16  32  64  ......
--------------------------------
1  5  17  49  129  ........  ?
'''


# 算出該行某一列的數字
def count_row_num(n, c):
	if n == c:
		return 2**n - 1
	return count_row_num(n+1, c) - 2**(c-(n+1))


n = int(input("請輸入要算第幾列的總和："))  # 第幾行
ans = 0
for i in range(1, n+1):
	ans += count_row_num(i, n)
print(ans)
