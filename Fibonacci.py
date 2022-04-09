
first_number =0
second_number =1
numbers=[0,1]


def fibonacci(n):
    
    # making the two variable accssible by the function
    global first_number ,second_number
    
   
    
    if n==1 :  #if only one ffibonacci number needed, return 0
        
        return numbers[:1]
        
        
    elif n==2:  
        
        return numbers
        
    
    else:
        
        hold=first_number
        first_number=second_number
        second_number += hold
       
        b.append(second_number)
        return fibonacci(n-1)
        
        
#print(fibonacci(10))

#print(fibonacci(5))

           
         
             
         