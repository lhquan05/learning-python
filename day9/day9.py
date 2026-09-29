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

"""
-Format dictionary la key:value, moi cap key:value dc goi la item
-remove

-pop
-laasy value tu key
-scan lan luot bang for
"""
# In person co bao nhieu key, va in tat ca value cua tung key do
person['job'] = 'accountant'

person['skills']=['React'] #gán đè lên nên skill từ 2 cái giờ thành mỗi "React"

person['skills'].append("JavaScript")#thêm vào 

person['skills'].append("MongoDB")#append chỉ thêm dc 1 kh thêm dc 2, Nếu muốn thêm hai thêm dạng list

addtional_skills=['Python','Node']

person['skills'].append(addtional_skills)#append dưới dạng list thành nested list nên hơi bị xấu

print(person)


dem_key=0
for key, value in person.items():
    
    dem_key+=1
      
    print(key,value)
    
print(dem_key)

print("so luong key: "+str(len(person)))


print(person['address'])        

print(person['country'])

print(person.get('country'))#thay vì ngoặc vuông dùng chữ(ngôn ngữ cấp cao)

print(person.pop('skills')) #xóa cả toàn bộ item skills, ở đây trả về những cái đã xóa

deleted_item=person.pop('country')

print(deleted_item)

person.popitem()#khác vs list

#caution ko có remove

# person.clear()#chừa dấu ngoặc

# del person#xóa cả dấu ngoặc và toàn bộ dict, dẫn tới kh print dc person

key_list= person.keys()

value_list= person.values()

print(key_list)

print(value_list)

print(person)
