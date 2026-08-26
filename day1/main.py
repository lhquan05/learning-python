import math
def main():
    
    print("Hello World!")
    name=str("Quan")
    
    title= "toi ten la:"
    age=29
    print("toi "+str(age) + " tuoi")
    print(title+name)
    x=8
    print(x)
    print(x+27)
    print(x*5+2)
    print(40/7)
    print(2**3)
    print(math.pi)
    r=3
    print(math.pi*(r**2))
    q=8 
    n=2
    print(math.log(q,n))
    print(math.pow(2,3))
    print(math.sqrt(121))
    Brian=age+1
    
    print("toi "+str(Brian)+" tuoi")
    Brian=Brian+1
    print(Brian)
    []
    t=27
    c=t+7
    print("tuoi cua chi 20 nam truoc la:"+ str(c-20))   
   
    
    
""" 
1 lop 10 ng vs 10 ten khac nhau va 10 tuou khac nhau 
in ra tat ca ten tren cung 1 dog cach nhau boi dau phay, bang nhieu cach 


ham cong tong so tuoi may ng o tren
ten ham la tuoi(), khi goi ham phai in tong so tuoi mn
co the dung google va convention han che chat gpt
"""
    
   
    
    
    
"""
hiện nay tuổi bố gấp 4 lần tuổi con . 3 năm trước , tổng số tuổi của 2 bố con là 39 tuổi . tính tuổi mỗi người ?
"""    
def ds():    
   emptyList=[]#list rỗng 
   studentlist=["an","bình","hà","phương","quân","Minh"]#hần tử dc đánh dâus từ 0 trái sang phải
   print(studentlist)
   print(studentlist[3])
   print(studentlist[:])
   print(studentlist[1:3])#lấy từ 1 đến bé hơn 3
   #thêm phần tử vào list
   studentlist.append("Tuấn")
   print(studentlist)
   #chèn vào vị trí
   studentlist.insert(2,"Ngọc")
   print(studentlist)
   studentlist[len(studentlist):]=["nami"]#chèn vào cuối, vs len là độ dài của tập hợp 
   print(studentlist)
   #đếm count
   print("đếm quân: ", studentlist.count("quân"))
   #dùng remove để xóa theo tên
   #dùng pop để xóa theo vị trí
   #đảo ngược list
   studentlist.reverse()
   print(studentlist)
   #sắp xếp theo abc, or số 
   studentlist.sort()
   print(studentlist)
   #xếp ngược
   studentlist.sort(reverse=True)
   print(studentlist)
   
  
   
   

# ds()    


def loop():
  n=10 
  for i in range(n):
    print(i)
    #cách 1
  studentlist=("an","bình","hà","phương","quân","minh","tuấn","phúc","ánh","thảo")
  print(type(studentlist))
  print(studentlist)
  # cách 2 dùng list
  studentList=["bình","hà","phương","quân","minh","tuấn","phúc","ánh","thảo"]
  print(type(studentList))
  print(studentList)
  # #Th1 tuôi bằng nhau hết
  # so hoc sinh= int(input("Nhập vào số hs: "))
  # i=0
  # tuoi=0
  # while(i==so hoc sinh):
  #   tong so tuoi= 15*i
  #   print("tuoi = ", tong so tuoi)
    
  
loop()
