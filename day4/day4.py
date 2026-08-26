def main():
    print ("Hello Word")
    person_info = {
   'firstname:':'Asabeneh',
   'lastname:':'Yetayeh',
   'country:':'Finland',
   'city:':'Helsinki'
    }
    print(len(person_info))
    
    #format của dictionary: 
    # 'key':'value'
    # hw: output: 
    # thông tin ng dùng:
    #in 4 thông tin thành 4 hàng không có ngoặc  
    print(person_info['city:'])
    for x, y in person_info.items():
        
        print(x,y)
        
          
if __name__ == "__main__":
    main()