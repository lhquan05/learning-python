# Ex:
#     Tạo chuỗi tên và chuỗi tuổi tương ứng
#     In ra chuỗi danh sách theo mẫu: 
#         a:14 ,b:23, c:34, ...

studentList=["Quân","HPhương","Hà","Tuấn","Như"]

age=["18","24","29","30","33"]

     

tuoi=""

dsach=""

for name in studentList:
    for tuoi in age:
        dsach=dsach+name+": "+tuoi
    
print(dsach)





# primes = [2, 3, 5, 7]
# for stt in range(10,2,-1):          # range(6)      #Từ 0 < max
#                                     # range(2,4)    #Từ min < max
#     #break      = Thoát khỏi vòng lặp ngay LẬP TỨC
#     #continue   = Bỏ qua nội dung BÊN DƯỚI, và tiếp tục vòng lập
    
#     if stt == 5:
#         continue        # 10,9,8,7,6,5,4,3 -> Wrong
#                         # 10,9,8,7,6,continue,4,3              
#         #break          # 10,9,8,7,6,break.
        
#     print(stt)
#     a=10            # Gán = declare, assign 
    
#     c=12
#     d=a+c
#     a=d         # assign
        
