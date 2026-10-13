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


    







if __name__ == "__main__":
    sum = add_two_nums("quân", "phúc")
    print(sum)
    dien_tich=area_of_circle(4)
    print(dien_tich)
    
