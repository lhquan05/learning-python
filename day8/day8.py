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

print(person['skills'][0])

print(person['address']['zipcode'])


"""
* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
*       If a person skills has only JavaScript and React, 
*           print('He is a front end developer'), 
*       if the person skills has Node, Python, MongoDB, 
*           print('He is a backend developer'), 
*       if the person skills has React, Node, Python and MongoDB 
*           Print('He is a fullstack developer'), 
*       else print('unknown title') - for more accurate results more conditions can be nested!
* If the person is married and if he lives in Finland, print the information in the following format: 
            Asabeneh Yetayeh lives in Finland. He is married.
"""
#requirement 1
if 'skills' in person:
    middle_index = int(len(person['skills'])/2)
    print(type(middle_index))
    print(person['skills'][middle_index])
else:
    print("kh co skills")


#######################################################
job=""
#requirement 2    
if 'skills' in person:
    
    print("pass vòng 1")
    
    if 'Python' in person['skills']:
        
        print("tuyen thẳng")
    
    else:
        print("chờ xét duyệt")
else:
    print("loai lun")
    
 ########################################################################################   
#requirement 3
print("requirement 3 - METHOD 1: ")
if 'skills' in person:
    print("nguoi này có skill")
    
    if 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills'] and 'React' in person['skills'] and 'JavaScript' in person['skills']:
        
        job = 'fullstack developer'
        
        # print("anh ay la: " + person['Job']) 
        
    elif ('Node' in person['skills']) and ('Python' in person['skills']) and ('MongoDB' in person['skills']):
        
        job = 'backend developer'
        
        # print("anh ay la:" + person['Job'])
        
    elif ('JavaScript' in person['skills']) and ('React' in  person['skills']):
    
        job ='front end developer'
        
        # print("anh ay la: "+person['Job'])
        
    else:
        job = "Unknown tile"
    
    # Sau khi xét duyệt hết rồi in ra 1 lần
    print("anh ay la: " +  job)
  
#requirement 3 - METHOD 2

print("requirement 3 - METHOD 2: ")
if 'skills' in person:
    if len(person['skills']) == 2:
        if ['JavaScript', 'React'] in person['skills']:
            job = 'front end developer'
        else:
            job = "Unknown tile"

    else: #Có nhiều hơn 2 skills
        if ['Node', 'Python', 'MongoDB'] in person['skills']:
            #Thằng này chắc chắn là backend rồi, nhưng mà hỏi thêm xme có skill fullstack không
            if ('React' in person['skills']):
                job = 'full-stack developer'
            else:
                job = 'back-end developer'
        else:
            job = "Unknown tile"
 
            
    print("anh ay la: "+  job)

####################################################     
    
    if ('Finland' in person['country']) and ('is_married' == True):
        
        thong_tin=f"Asabeneh Yetayeh lives in {person['country']}. He is married."
        
        print(thong_tin)
        
    else:
        
        print('chua ket hon')
        
print(person)        

    
    
        
    
    
    
    
    