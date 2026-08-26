import time

def main():
                   #0
    studentlist=["Quan","Phuc","HPhuong","Như","Thông"]

    i=0  #index
    if i < len(studentlist):
        print(studentlist[0])       # Truy xuat phan tu mang, list Access array's element, list's element
    
    dsachtuoi=[15, 16, 19, 20, 25]

    dsach=""

    giay=0
    # i=""                  # DƯ Chứ kh sai 

    size=len(studentlist)

    print(type(size))
    countTong=0
    
    #===============================================================
    for i in range(len(studentlist)):
        
        if giay == len(studentlist)-1:
            
            dsach =  dsach + studentlist[i] + ":" + dsachtuoi[i] + "."
        
        else:
            
            dsach = dsach + studentlist[i] + ":" + dsachtuoi[i] + ","
            
        giay = giay + 1
        
        countTong= countTong + 1
        
    print(countTong)
    print(dsach)
    
    #===============================================================
    dsach2=""
    countTen=0
    countTuoi=0
    countTong=0
    for name in studentlist:                # For Ten 
        dsach2 = dsach2 + name + ":"        # --> countTen=0, countTuoi=0
        
        #########for trong#############
        for tuoi in dsachtuoi:              #for Tuoi
            if countTen == countTuoi:                   # l0 --> countTen=0, countTuoi=0        countTen=1, countTuoi=0    countTen=2, countTuoi=0  
                dsach2 = dsach2 + tuoi + ", "           # l1 --> countTen=0, countTuoi=1         
                break                                   # l2 --> countTen=0, countTuoi=2        
                                                        # l2 --> countTen=0, countTuoi=3
                                                        # l2 --> countTen=0, countTuoi=4
                                                        # dsach2=Quan:15, 
                                                        
            countTuoi = countTuoi + 1
            countTong = countTong + 1
       
        
        print("For trong da chay xong!")
        countTuoi = 0
        print(countTuoi)
        
        #########for trong#############
        
        
        countTen = countTen + 1                 # countTen = 1
        countTong = countTong + 1
    ##############################################        
            
    print(dsach2)        
    print(countTong)
        
        
        
if __name__ == "__main__":
    main()