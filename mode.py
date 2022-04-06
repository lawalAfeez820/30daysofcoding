   #create the list of unique number



def modal(list_of_numbers):
    
    modal_class=[]   # hold the most occuring values
    
    count_dict={}  #to hold the value and the number of occurence of each unique numbers
    
    unique = set(list_of_numbers) #create a set of unique numbers
          
    for i in unique: #iterate over the unique values
        
        count= list_of_numbers.count(i) #save the most number occurence of each unique value
        
        count_dict[i]=count #assigning the number of occurence to each unique value
        
    mode=max((count_dict.values())) #catch the highest occurence
    
    for i in count_dict: #iterate over the dictionary
        
         if count_dict[i] == mode: # check the values  that as the same occurrence as the mode
             
             modal_class.append(i) #if true, put in the modal_class list
    
    return modal_class  #output the modal_class
  
        
  #check    1  
   
#print(modal(["a", "b", "a", "a", 3, 3, 2, "hello", "b"]))

#ouptut 1 = ["a"]

    
 # check 2  
    
#print(modal(["a", "b", "a", "a", 3, 3, 2,3 ,"b","hello", "b"]))

#output 2 = ["a","3","b"]
