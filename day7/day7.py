fruits=("cam","xoai","buoi","man")

# print(fruits[2])

# print(fruits[len(fruits)-1])

# print(fruits[0])

for traicay in fruits:
    print(traicay)
    if traicay == "xoai":
        break
    
print(fruits[1:3])    

print(fruits[0:])  #đây gọi là slicing và áp dụng dc cho list lun, có thể xài số âm, string lun

a="Hai:23"

print(a[0:len(a)-3])

a=list(fruits)

print(type(a))

"""
    In menu gồm 3 options: 
        1. Đếm số lượng phần tử
        2. Xoá phần tử cuối cùng 
        3. Thêm phần tử mới vào cuối danh sách -> Yêu cầu nhập thêm content của phần tử => in ra
        
    Tạo input gán vào biến tên select. Đọc input từ bàn phím
    select=1
    
    select=3
    content= 
    
    Tạo tupple/list gồm 10 phần tử bất kì
    
    Điều kiện là chạy liên tục: sau khi thưck hiện xogn 1 option thì hỏi option tiếp theo liền
            (chỉ bấm duy nhất 1 lần F5 để chạy, nếu muốn thoát bấm Pause hoặc là Ctrl+C dưới Terminal để thoát)
        
        Gợi ý dùng for
        
"""




