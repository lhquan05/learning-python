person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
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
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node, Python and MongoDB Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.
"""
#requirement 1
if 'skills' in person:
    print(person['skills'][2])
else:
    print("kh co skill")


#######################################################

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
if 'skills' in person:
    print("nguoi này có skill")
    
    if 'JavaScript' in person['skills'] and 'React' in  person['skills']:
        
        person['Job'] = 'front end developer'
        
        print("anh ay la: " + person['Job']) 
        
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        
        person['Job'] = 'backend developer'
        
        print("anh ay la:" + person['Job'])
        
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills'] and 'React' in person['skills'] and 'JavaScript' in person['skills']:
        
        person['Job'] ='fullstack developer'
        
        print("anh ay la: "+person['Job'])
        
    else:
        print('unknown title')
        
   ####################################################     
    
    if 'Finland' in person['country'] and 'is_married':
        
        thong_tin=f"Asabeneh Yetayeh lives in {person['country']}. He is married."
        
        print(thong_tin)
        
    else:
        
        print('chua ket hon')
        
print(person)        

    
    
        
    
    
    
    
    