def is_leap(year):
    leap = 'false'
    if(year%400==0 and year%100==0):
        print("leap=True")
    elif(year%4==0 and year%100!=0):
        print("leap = True")
    else:
        print("not a leap year")
    return leap
    
    

    
         
