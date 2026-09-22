fruits=("cam","xoai","buoi","man")

# print(fruits[2])

# print(fruits[len(fruits)-1])

# print(fruits[0])

for traicay in fruits:
    print(traicay)
    if traicay == "xoai":
        break
    
print(fruits[1:3])    

print(fruits[0:])  #đây gọi là slicing và áp dụng dc cho list lun, có thể xài số âm, string lun

a="Hai:23"

print(a[0:len(a)-3])

a=list(fruits)

print(type(a))






