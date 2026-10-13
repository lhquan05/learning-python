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
seen=0

while i<=4:
    
    name=input("please enter ur name: ")

    applicants_list.append(name)

    print(applicants_list)
    
    visa_question=input("have u been in UK before: ")
    
    answers=visa_question.lower()
    
    if answers == "yes":
        seen = (seen << 1) + 1
        
        i+=1
        
        print(seen)
    elif answers == "no":
        
        seen = seen <<1 
        
        i+=1
        
        print(seen)
    else:
        print("Sai cú Pháp. Vui lòng nhập lại")
    
   
print("ket qua la:", seen)
    




