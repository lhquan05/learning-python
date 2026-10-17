"""
1.Declare a function add_two_numbers. It takes two parameters and it returns a sum.
2.Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
3.Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
    Check if all the list items are number types. If not do give a reasonable feedback.
4.Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
    Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
5.Write a function called check-season, it takes a month parameter and returns the season:
    Autumn, Winter, Spring or Summer.
6.Write a function called calculate_slope which return the slope of a linear equation
7.Quadratic equation is calculated as follows: ax² + bx + c = 0. 
    Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
8.Declare a function named print_list. 
    It takes a list as a parameter and it prints out each element of the list.
9.Declare a function named reverse_list. 
    It takes an array as a parameter and it returns the reverse of the array (use loops).
"""
#parameter = input
#Câu 1

def add_two_nums(input1, input2):
    sum= 0
    sum = input1 + input2
    return sum



#Bài 2
import math

def  area_of_circle(r):
    area = 0
    area = math.pi * (r**2)
    return area



#Bài 3

def add_all_nums (a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        
        print("tất cả đều là kiểu number")
        
        sum = a + b 
        
        return sum
    
    else:
        print("không đúng format nên không thể cộng")
    
        

#Bài 4
def convert_celsius_to_fahrenheit(C_degree):
     
     F= (C_degree * 9/5) + 32
     return F
 
     
#Bài 5 
def check_season(month):
    if 1 <= month <= 3:
        return "spring"
    
    if 4 <= month <= 6:
        return "summer"
    
    if 7 <= month <= 9:
        return " fall"
    
    if 10<= month <= 12:
        
        return "winter"
    
    else: 
        print(" sai định dạng")
    
    
#Bài 6

def  calculate_slope(a, b):
    return a


#Bài 7 

def Quadratic_equation(a, b, c):
    delta = b**2 - 4*a*c
    x1 = 0
    
    x2=0 
    
    x=0
    
    if delta == 0:
        print("phương trình có nghiệm kép")
        
        x  = -b / (2*a)
        
        return x
    
    if delta > 0:
        print("phương trình có 2 nghiệm phân biệt")
        
        x1 = -b + math.sqrt(delta) / (2*a)
        
        x2 = -b - math.sqrt(delta) / (2*a)
        
        return x1, x2
        
    
    else: 
        print("ptrinh vô nghiệm")
        
        


    







if __name__ == "__main__":
    sum = add_two_nums("quân", "phúc")
    print(sum)
    dien_tich=area_of_circle(4)
    print(dien_tich)
    
    #Bài 3
    
    number_check = add_all_nums("2", 4)
    
    print("tổng của các number = ", number_check)
    
    #Bài 4
    Nhiet_do=convert_celsius_to_fahrenheit(5)
    
    print(Nhiet_do)
    
    #Bài 5
    mua = check_season(6)
    
    print(mua)
    
    #Bài 6
    slope =  calculate_slope(3, 2)
    
    print(slope)
    
    #Bài 7
    
    x1, x2 = Quadratic_equation(1, 4, 2)
    
    print( "x1 = ", x1 )
    
    print( "x2 = ", x2)
    
    
    