def main():
    print ("Hello Word")
    person_info = {
        'firstname:':'Asabeneh',
        'lastname:':'Yetayeh',
        'country:':'Finland',
        'city:':'Helsinki'
    }
    
    Quan_info={
        'firstname:' : 'Quan',
        'lastname'   : 'Le' ,
        'country' : 'america',
        'city' : 'Dortmund'
        
    }
    
    Phuc_info={
            'firstname:' : 'Phuc',
            'lastname'   : 'Le' ,
            'country' : 'Germany',
            'city' : 'Augsburg'
            
        }
    
    print(len(person_info))
    personList=[{
        'firstname:':'Asabeneh',
        'lastname:':'Yetayeh',
        'country:':'Finland',
        'city:':'Helsinki'
    }, {
        'firstname:' : 'Quan',
        'lastname'   : 'Le' ,
        'country' : 'america',
        'city' : 'Dortmund'
        
    } 
    ]
    print(len(personList))
    personList.append(Phuc_info)
    print(personList[2])
    
    personList.append({
            'firstname:' : 'Phuc2',
            'lastname'   : 'Le2' ,
            'country' : 'Germany2',
            'city' : 'Augsburg2'
            
        })
    
    
    
    # personList.remove({
    #         'firstname:' : 'Phuc2',
    #         'lastname'   : 'Le2' ,
    #         'country' : 'Germany2',
    #         'city' : 'Augsburg2'
            
    #     })
    # PersonList.remove(PersonList[2])
    
    # del personList[2]
    
    
    # PersonList.remove(PersonList[len(PersonList)-1])
    
    
    # user1=personList.pop()
    
    # print(user1)
    
    
    # personList.clear()
   
    # del personList #khi xóa List bằng del thì cả List và phần tử sẽ biến mất khiến cho print ở line 105 bị lỗi. 
    
    back_up=personList.copy()
    
    TotalList=back_up + personList
    
    
    # print(back_up)
    
   
    print(TotalList)
    
    print(len(TotalList))
    
    
    
    
    
    
    # print(personList)
    
    
    
    
            
    
    #format của dictionary: 
    # 'key':'value'
    # hw: output: 
    # thông tin ng dùng:
    #in 4 thông tin thành 4 hàng không có ngoặc  
    # print(person_info['city:'])
    # print(person_info['firstname:'])
    # print(person_info['firstname:'])
    
    # for x, y in person_info.items():
        
    #     print(x,y)
    
        
          
if __name__ == "__main__":
    main()