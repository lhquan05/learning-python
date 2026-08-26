def main():
    
    studentlist=["Quan","Phuc","HPhuong","Như","Thông"]

    dsachtuoi=[15, 16, 19, 20, 25]

    dsach=""

    giay=0
    # i=""#DƯ Chứ kh sai 

    size=len(studentlist)

    print(type(size))
    
    for i in range(size):
        
        if giay ==len(studentlist)-1:
            
            dsach =  dsach + studentlist[i] + ":" + str(dsachtuoi[i]) + "."
        
        else:
            
            dsach= dsach + studentlist[i] + ":" + str(dsachtuoi[i]) + ","
        giay = giay + 1

        
    print(dsach)
   
        
        
        
        

if __name__ == "__main__":
    main()