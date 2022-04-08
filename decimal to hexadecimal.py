RemMoreThan9 ={10:"a" ,11:"b",\
 12:"c", 13:"d", 14:"e", 15:"f"} #dictionary of remainder greater than 10
 
 
def dec_to_hexa(number):
    
    number=str(number)
    
    if  not number.isnumeric():
        raise AssertionError("input must not contain alphabet")    #raise error if number contain alphabet
        
    else:
        
        number = int(number)
    
        arrangement=""  #to store the remainder
    
        for i in range(2,number): 
    
            if number <16**i :
                c=i
                break
            elif number== 16**i:
                c=i+1
                break
           #the above iteration help to confirm in number of time 16 is going to divide the number given.
        
    
    
        for i in range(int(c)):
    
    
    
            number,remainder=int(number/16) ,number%16  #updating the number given on every division performed and also the remainder variable save the remainder
            
            
    
            if remainder in RemMoreThan9:
                arrangement= ((arrangement))+RemMoreThan9[remainder]
         
         # if the remainder is greater than 9, if should replace it with it corresponding value in the dictionary 
        
            else:
    
                 arrangement = arrangement+str(remainder)
    
    rearrangement=arrangement[::-1]
    #rewrite the number from bottom to top
 
    
    
    
    return (rearrangement)
     
print(dec_to_hexa("4906"))