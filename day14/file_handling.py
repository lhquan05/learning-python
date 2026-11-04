#De Bai: in toan bo noi dung trong file input.txt
def read_and_print_size(file_name):
    
    file_opening =open(file_name,'r')#phai co folder chua no 

    Inhalt = file_opening.read(-1)#mot la de default hai la phai de negative parameter la doc het 

    print(Inhalt)

    size_inhalt = len(Inhalt)
    print(size_inhalt) #Phim enter cx la 1 ki tu lun

    file_opening.close()#phai dong roi mo thi may tinh moi hieu, ko mo 2 lan lien tiep

# file_opening =open('day14/input.txt','r')

# halb_Inhalt = file_opening.read(size_inhalt // 2)
# print(halb_Inhalt)

# file_opening.close()
def readling_first_line():
    
    file_opening =open('day14/input.txt','r')

    first_line = file_opening.readline()#ham doc chi moi first line, neu bo ki tu vo no dem character.

    print(type(first_line))# ham read va readline luon tra ve kieu string

    file_opening.close()


def print_each_line(file_name):
    file_opening =open(file_name)
    
    list_of_line = file_opening.readlines()
    
    print(type(list_of_line))
    
    print(len(list_of_line))
    i= 0
    for line in list_of_line:
        i +=1
        print("line" + str(i) +":" + line)
        
    
    file_opening.close()
#Goi ham 

read_and_print_size('day14/input.txt')
read_and_print_size('day14/input2.txt')


print_each_line('day14/input.txt')
print_each_line('day14/input2.txt')

