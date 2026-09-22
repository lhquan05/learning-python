# Reuse the employee list and position from day 5
# Do the following requirements:
#  - Tạo biến current_year = 2026.
#  - người A2 nghĩ việc, xoá tên họ khỏi cty 
#  - Năm mới => Mỗi người tăng lên 1 tuổi. Chỉ khi current_year = 2027
#  - In ra câu "Chuc mung sinh nhat lan thu Tuoi cua Ten"
#  - Position cũng tăng lên theo. Ex: Nhân viên -> Leader..... , 
#  - There should be two giam doc in the company
#  - Print the whole company's list.

#####!!!!!!!!!!!!: Gán đúng vị trí. Tăng tuổi theo số năm tương ứng nhập vào


onboard_year=2026


current_year=int(input("Nam:"))

year_passed= current_year - onboard_year

employee_list=[{
            'Ten': "A1",
            'Tuoi' :20, 
            'Position':""
        },
        {
            'Ten': "A2",
            'Tuoi' :20,
            'Position':""
        },
        {
            'Ten': "A3",
            'Tuoi' :20,
            'Position':""
        },
        {
            'Ten': "A4",
            'Tuoi' :20,
            'Position':""
        },
        {
            'Ten': "A5",
            'Tuoi' :20,
            'Position':""
        }]

postion=("giám đốc","accountant","manager","leader","nhân viên")

nv_1 = employee_list[0]
nv_2 = employee_list[1]
nv_3 = employee_list[2]
nv_4 = employee_list[3]
nv_5 = employee_list[4]

nv_1['Position'] = postion[0] # Lấy tuple ra gán vào dict
nv_2['Position'] = postion[1] # Lấy tuple ra gán vào dict
nv_3['Position'] = postion[2] # Lấy tuple ra gán vào dict
nv_4['Position'] = postion[3] # Lấy tuple ra gán vào dict
nv_5['Position'] = postion[4] # Lấy tuple ra gán vào dict




print(type(employee_list))
print(type(postion))



# count=0


# for name in employee_list:
    
#     print(name)
#     print(type(name))
    
#     if name['Ten'] == "A2":
    
#         employee_list.remove(employee_list[count])
#         break
    
#     count+=1
        

# print(employee_list)


################################

#step 1: là đi tra từng người tên j bnhieu tuổi
#step 2: biết bnhieu tuổi
#step 3: cộng  lên theo year
#step 4: ghi vào lại list 
#step 5: in ra "Chuc mung sinh nhat lan thu Tuoi cua Ten"
for employee_age in employee_list:
    employee_age['Tuoi']+= year_passed

    chuc_mung=f"Chuc mung sinh nhat lan thu {employee_age['Tuoi']} cua {employee_age['Ten']}"
    
    print(chuc_mung)

i=0
for ten_tuoi in employee_list:
   
    
    # ten_tuoi['Tuoi']+=1
    
    if current_year == 2027:
    
        ten_tuoi["Tuoi"]= ten_tuoi["Tuoi"] + 1
    
        chuc_mung=f"Chuc mung sinh nhat lan thu {ten_tuoi['Tuoi']} cua {ten_tuoi['Ten']}"
    
    
        print(chuc_mung)
        
    promotion = ten_tuoi["Position"]
        
    if ten_tuoi["Position"]=="nhân viên":
         continue
                
    if (i < len(postion) - 1):
        ten_tuoi["Position"]=postion[i+1]
        
        i= i+1
        
        
        
     
print(employee_list)
       
    
    # print(ten_tuoi["Tuoi"])
    
    #B1: lấy vị trí 
    #B2; check vị trí thằng kế
    #B3: gắn vào thanwf hiện tại
    