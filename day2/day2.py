import math
def main():
    print("Hello World!")
    
    studentList=["quan","phuc","tuan","ha","phuong"]
    print(studentList)          #In toàn bộ định nghĩa của studenList
    
    dsach=""
    dsach2=str()
    
    print(type(dsach2))
    
    so=3456
    epso=str(so)                #Ép một biến về kiểu string
    
    chuoiso="1234"              #Chuỗi số, không có khả năng thưc hiện phép toán
    chuoiso2=str(1234)          
    print(chuoiso)
    print(chuoiso2)
    
    print(type(dsach))
    
    to_giay = 0 #Ban dau khoi tao bang 0 mà không phải là ""
                # Vì số lần là kiểu SỐ (integer) để thực hiện phép tính 
    
    for name in studentList:
        # dsach = dsach + name + ", " 
        
        # CACH 1
        # Nếu name=phuong thì không chèn ", "
        # Ngược lại thì chèn ", "
        # if name == "phuong":
        #     #khong chen
        #     dsach = dsach + name
        # else:
        #     #chen
        #     dsach = dsach + name + ", " 
        
        # CACH 2
        # Nếu name đang là phần cuối cùng (thứ 4) thì không chèn ", "
        # Nếu bốc lần cuối cùng thì không chèn 
        # Ngược lại thì chèn ", "
        
        if to_giay == 4:
            # Lần cuối cùng k chèn
            dsach = dsach + name
        else:
            # Chèn
            dsach = dsach + name + ", " 
            
        to_giay = to_giay + 1   # Tăng biến đếm số lần lên 1 ở mỗi lần loop
        
        
    print(dsach)  
    print(to_giay)
       
    """
        bryan=bryan+1
        hientai =  truoc do + 1
        
        dsach = dsach + name + , 
        htai = truocdo + name
        
        for: 
            so lan chay: 5 lan 
        L1: name=quan
            dsach=""+quan = quan
        L2: name=phuc
            dsach=quan+phuc = quanphuc
        L3: ....
        
        End Loop
        dsach = quan, phuc, tuan, ha, phuong

        print(dsach)
    """
    age=[15,18,10,20,21]
    totalage=0
    for tuoi in age:
        totalage= totalage + tuoi

    print(totalage)
   
if __name__ == "__main__":
    main()