result=[]   #create the list of unique number

def list_to_set(list_of_numbers):
    
    for i in list_of_numbers: #iterate through the list
        
        if i not in result:  #check for unique value
            
            result.append(i)
    
    return result
    
print(list_to_set(["a", "b", "a", "a", 3, 3, 2, "hello", "b"]))