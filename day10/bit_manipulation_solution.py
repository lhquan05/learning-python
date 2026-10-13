"""
-Tạo 1 list applicants, yêu cầu dùng input nhập vào : tên, và trả lời câu hỏi 
"have u been in the UK before?"
người dùng sẽ trl là Yes or No(chấp nhận tất cả thể loại yes no, gợi ý dùng hàm lowercase/uppercase )
-Tên ghi trong applicant list 
câu trl lưu trong 1 biến ở định dạng nhị phân trong đó mỗi ng chiếm 1 bit của biến đó. 

vdu: Đặt biến tên seen = '0011' có nghĩa là trong 4 ng thì 2 ng cúi cùng yes và 2 ng đầu no 
 
"""
applicants_list=[]
i=0
seen="" 
count=0
seenShift=0

while i<=4:
    
    if len(applicants_list) == count:
        name=input("please enter ur name: ")
        applicants_list.append(name)
        
    
    visa_question=input("have u been in UK before: ")
    
    answers=visa_question.lower()
    
    i+=1
    
    if answers == "yes":
        # chèn số 1 vào seen
        count = count + 1       
        seenShift = (seenShift << 1) + 1
        
        """
            0b00000000 = 0
            0b00000001 = 0 + 1
            0b00000011 = (0b00000001 << 1) + 1
                        0b00000010 +      
                        0b00000001 
                        =0b00000011
            0b00000101 = 4 + 1
        """
    elif answers == "no":
        # chèn số 0 vào seen 
        count=count+1
        seenShift = seenShift << 1
    else:
        #Yều cầu nhập lại 
        print("Vui long tra loi lai cau hoi! Sai dinh dang!")
        None

print(applicants_list)
print("seenShift (int)=" + str(int(seenShift)))
print("seenShift (int)=" + str(type(seenShift)))
print("{0:b}".format(seenShift)) #convert int to binary

#Extra: Đếm số người trả lời YES
#1100 = 12 -> 2 = 2^2+2^3
#1010 = 10 -> 2
#1111 = 15 -> 4
#0111 = 7
#1000 = 8 -> 1
countBit1=0
while seenShift > 0:
    if seenShift % 2 == 0: #Chia lấy phần dư
        #khong du = so chan = binary ket thuc la 0
        None
    else:
        #du = so le = binary ket thuc la 1
        countBit1+=1
        
    #chia đôi để dịch qa phải 1 bit
    seenShift = seenShift // 2 #Chia lấy phần nguyên 
    
    #11110  : count=0
    #01111  : count=1
    #00111  : count=2
    #....
    
print("Co " + str(countBit1) + " ng tra loi YES")

# seen="" string.  "10101010" -> tốn 8 byte để lưu đc 8 người
#             mỗi một 0,1 là 1 kí từ đc cấu thành ít nhất là 8 bit ~ 1 byte 

# seenShift int - 10101010 : 
#                  Mỗi một 0,1 là 1 bit
#int64= max int64  = 64 bit = 8 byte ~ lưu đc 74 người 




