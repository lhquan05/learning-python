menu=["rice","noodle","pho",'banh','com','bun','mien','comsuon','nui','bo','ga']

print(menu)

i=1

phuc=True
"""
khi nào nhắc đến infinitive thì nghĩ ngay đến WHILE(TRUE):
"""    
# for i in range(10): for là vòng lặp biết trc số lần 
# while(i>0):
# while(2>0):
#while(true):
while(phuc):#gan true vao bien giong voi cai tren


    


    #x1= chỗ có thể đặt select
    select=int(input("Nhap du lieu:"))  
    
    if select==1:
        print("so phan tu la:",len(menu))
        
       
    
    elif select ==2:
        if len(menu)==0:
            print("menu da rong vui long kh nhap 2")
            
        
            continue
        
        print("xoa phan tu:",menu.pop())
        
        print(menu)
        
    elif select ==3:
        new_food=input("nhap them mon an moi:")
        
        menu.append(new_food)
        
        print(menu)
    
    #x2=đặt select ở đây hoặc x1
    # select=int(input("Nhap du lieu:"))

        
    
    
   
   
    
    

    
    
    
    
    

    
    