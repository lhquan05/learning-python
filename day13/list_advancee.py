password="Quan1234"

input_list = []



for element in password:
    print(element)
    
    input_list.append(element)
    
print(input_list)
##########################################################################################
# List Comprehension
# syntax: [expression for i in iterable if condition]
##########################################################################################
new_List = [i for i in password ]

print(new_List)
##########################################################################################
#Input_List chi bao gom characters
input_list2 = []

for element in password:
    print(element)
    
    
    # if element.isnumeric():#check kieeur so      #cach 1
        
    #     continue
    
    # if element >= '0' and element <= '9':        #cach 2
    if ord(element) >= 48 and ord(element) <= 54:  #cach 3
        continue
    
    
    input_list2.append(element)
    
print(input_list2)
#################################################################################
new_List2 = [i for i in password if i.isnumeric() == False ] 

print(new_List2)
#################################################################################

#Taoj List tu 0 den 9 bang List Comprehension
new_List3 = [i for i in range (10)]

print(new_List3)

#Tao List tu 0 den 10 chi in so chan

new_List4 = [i for i in range(0, 11, 2)]

print(new_List4)

new_list5 = [i for i in range(10) if i % 2 ==1]

print(new_list5)

# Filter List 

number_list = [ 1, -1, 5, 6, 9, 12, -5, -6, -8, 0]


filtered_list = [ i for i in number_list if i % 2 == 0 and i>0]

print(filtered_list)

#flattening List 2d

List_of_Lists = [[5, 6, 7], [-1, -2, -5 ],[8, 9, 10]]

for sub_list in  List_of_Lists:
    for element in sub_list:
        print(element)
        


flattned_list = [element for sub_list in List_of_Lists for element in sub_list]

print(flattned_list)
