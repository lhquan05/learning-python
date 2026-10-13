#hàm ko input, ko return. 
def quan(): 
    print("Xin chào")
    


#hàm ko input, có return. 
def ham_return():
    a= 2
    b=4
    
    return (a*b)
    
ham_return()

c=ham_return()

print(c)

#Loại 3: có input và ko return
#ví dụ: hàm in tên chúc mứng sn
def ham_cong3(input1):
    
    phep_tinh = input1 + 3
    
    print(phep_tinh)

d= ham_cong3(7) # cách 1: bỏ thằng vào lun. 

print(d) # ra None tại ko có gì cả. 

#Loại 4 là có input và có return
def ham_loai4(input2):
    
    e= 3
    phep_tinh2 = input2 *e
    
    return(phep_tinh2)

ham_loai4(5)

cai_thung= ham_loai4(5)

print(cai_thung)
print(ham_loai4(5))

def kiem_tra_format_answers(answers):
    result= False
    #  B1: em lower nó xuống
    lower_answer= answers.lower()
    #  B2: em ktra yes/no
    if lower_answer == "yes":
        result = True
    elif lower_answer == "no":
        result = True
    else:
        result = False
    
    return (result)

answer= input("nhap vao day: ")
ket_qua= kiem_tra_format_answers(answer)

if ket_qua == True:
    print("Đúng format")
else:
    print("Sai format")
    
    

     