
# def <name>():

def Hello():
    # Loại 1: Hàm không có kết quả trả về - không có tham số đầu vào 
    #Tưởng tượng:
    #   Máy xay sinh tốt nhưng k bỏ trái cây,  và không có nước trả ra
    print("XIN CHAO")

    
def Get10():
    # Loại 2: Hàm có kết quả trả về - không có tham số đầu vào 
    # return <Kết quả trả quả> 
    return 10
def GetPersonInfo():
    person={
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_married': True,
        'skills': ['JavaScript', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    } 
    return person
    
def Loai3():
    # Loại 3: Hàm có kết quả trả về -  có tham số đầu vào 
    None
    
def Loai4():
    # Loại 4: Hàm không kết quả trả về -  có tham số đầu vào 
    None
    
def quan():
    print("Ham Quan is called")
    
def dem_bit_1():
    print("Ham dem_bit_1 is called")
    None

def nhap_data():
    print("Ham nhap_data is called")
    None
     
def main():
    print("Hello World!!!!")
    
    dem_bit_1()
    
    print("Doing something....")
    
    quan()
    
    ##Gọi hàm Get10
    result = 5 * Get10()
    
    print(result)
    
    personinfo = GetPersonInfo()
    print(personinfo)

# Cái để cho python biết bắt đầu từ đâu 
if __name__ == "__main__":
    main()      #Caller - Gọi hàm ra thực thi
    #quan()