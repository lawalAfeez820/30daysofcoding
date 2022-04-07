
def palindrome(number):
    count=0 #this variable count the  numbers of that are palindrome
    
    palindromes=list()   #This variable the the palindrome in a list
    
    for i in range(number): #iterate through the number given
        
        str_number = str(i) #convert each number less than the given number to a string
        
        if str_number==str_number[::-1]:
            # check for palindrome
            
            palindromes.append(str(i))
            #add the palindrome to the back of palindromes variable
            
            count+=1 
            
            
    palindromes = " ,".join(palindromes)
   #convert the palindromes list to string separated with space and comma
            
    return f"\tThe palindromes less than {number} is/are\n {palindromes}\n\n \tAnd they are\n{count} in number."
  
number = int(input("Enter the number you want to know the total number of palindrome that are less than the number and also to give the output those numbers: \n")) 

print(palindrome(number))


            