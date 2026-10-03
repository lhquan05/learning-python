a=1 #false
b=7 #true
result1=not(a and b)

print(type(result1))
print(result1)

result2=a or b#để không thì 1 cái thõa là dc nên b thỏa == true 

print(result2)
print(type(result2))

"""
a b r(AND)
0 0 false
0 1 false
1 0 false
1 1 true
kết luận: 1 nhân cho 0 thì bằng 0. 1 nhân cho 1 bằng chính nó

a b r(OR)
0 0 false
0 1 true
1 0 true: 
1 1 true
==> kết luận: 1 cộng(logic) 0 cgi cx == chính nó hết

kiểu "byte" == 8 bit 
1 bit = boolean (2 giá trị)

==>1 byte = 8 biến boolean
"""
print(int('00100001', 2))# số 2 là kiểu nhị phân, biểu diễn kiểu nhị phân thg 1 byte
print(int("101", 2))

import sys
x=8 # binary: 00001000

print(x.__sizeof__())
print(sys.getsizeof(x))
#dịch bit
print(chr(int('01100001', 2))) # 1 ký tự dc biểu diễn = 1 byte

"""
0b01100001

0b00000001 = 1
0b00000010 = 2
0b00000100 = 4
0b00001000 = 8

==> nhận xét với mỗi số 1 thì biểu thức tăng lên 2 mũ x ( x tương đương với vị trí của số 1).
==> khi bit 1 dịch qua trái 1 đvi thì kqua thập phân tăng lên GẤP ĐÔI.
==> khi bit 1 dịch qua phải 1 đvi thì kqua thập phân chia đôi.
"""
c=1
shiftL1= c << 1 # khi bit 1 dịch qua trái 1 đvi thì kqua thập phân tăng lên GẤP ĐÔI

print(shiftL1)

c=2
shiftL1= c << 2

print(shiftL1)

"""
-Tạo 1 list applicants, yêu cầu dùng input nhập vào : tên, và trả lời câu hỏi 
"have u been in the UK before?"
người dùng sẽ trl là Yes or No(chấp nhận tất cả thể loại yes no, gợi ý dùng hàm lowercase/uppercase )
-Tên ghi trong applicant list 
câu trl lưu trong 1 biến ở định dạng nhị phân trong đó mỗi ng chiếm 1 bit của biến đó. 

vdu: Đặt biến tên seen = '0011' có nghĩa là trong 4 ng thì 2 ng cúi cùng yes và 2 ng đầu no 
 
"""





