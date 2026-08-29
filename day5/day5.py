def main():
    student_list=["Quan","Phuc","Tuan"]
    
    student_list.append("HP")
    
    Ten="Hải"
    
    student_list.append(Ten)
    
    print(len(student_list))
    
    student_list.append({'Ten'  : 'Quan',
                         'Tuoi' : '27'})
    
    student_list.append(27)
    
    student_list.append(["Nhu","Thong"])
    
    student_list.append(2.5)
    
    
    print(student_list)
    
    for name in student_list:
        print(name)
        
def day5():

    bien = ("phuc97", "Phuc")
    
    quan=(2)
    
    bien_mat=()
    
    print(type(bien_mat))
    

    print(type(quan))
    
    print(type(bien))
    
    
    a=("quan", 5, 2.5 )
    
    # a.insert(1, "Phuc" )  Tuple ko có
    
    # a.append("hai") Tuple ko có
    
    # a.remove("quan")
    
    employee_list=[{
            'Ten': "A1",
            'Tuoi' :"20",
            'Position':""
        },
        {
            'Ten': "A2",
            'Tuoi' :"20",
            'Position':""
        },
        {
            'Ten': "A3",
            'Tuoi' :"20",
            'Position':""
        },
        {
            'Ten': "A4",
            'Tuoi' :"20",
            'Position':""
        },
        {
            'Ten': "A5",
            'Tuoi' :20,
            'Position':""
        }]
    
    postion=("giám đốc","accountant","manager","leader","nhân viên")
    
    #step 1: Lay cai dict ra từ List
    #Step 2: IN key của cái element vừa lấy ra
    #Step 3: Gán positions
    
    nv_1 = employee_list[0]
    nv_2 = employee_list[1]
    nv_3 = employee_list[2]
    nv_4 = employee_list[3]
    nv_5 = employee_list[4]
    
    print(nv_1['Ten'])
    print(nv_1['Position'])
    
    pos_nv1 = nv_1['Position']  #Lấy position từ nv1 ra gán vào biến pos_nv1
    
    """
    nv_1['Position'] = postion[0] # Lấy tuple ra gán vào dict
    nv_2['Position'] = postion[1] # Lấy tuple ra gán vào dict
    nv_3['Position'] = postion[2] # Lấy tuple ra gán vào dict
    nv_4['Position'] = postion[3] # Lấy tuple ra gán vào dict
    nv_5['Position'] = postion[4] # Lấy tuple ra gán vào dict
    """
    
    print(nv_1['Position'])
    
    print("Gan POS  cho Nhan Vien")
    
    i = len(postion) - 1
    for nv in employee_list:
        a = nv['Position']              # Lấy vị trí của nhân viên đó 
        nv['Position'] =  postion[i]    # tupple thứ i 
        i = i - 1
    
    
    # for x, y in nv_1.items():
    #     print(x,y)
    
    ################################################################
    for each_person in employee_list:
       
        print(each_person)
    

        
if __name__ == "__main__":
    # main()
    day5()