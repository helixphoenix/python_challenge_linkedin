from typing import List
def finder( search_list, search_item)-> List[List[int]]:
    N= len(search_list)
    indices_list=[]
    for i in range(N):
        if search_list[i] == search_item:
            indices_list.append([i])        
        elif isinstance(search_list[i], List):
            for index in finder(search_list[i], search_item):
                indices_list.append([i]+index)            
    return indices_list     

    # return print(indices_list )       
                
                           
 
    
   


example=[[[1,2,3],2,[1,3]],[1,2,3]]

fitifiti=finder(example,2)                        
            
print(fitifiti)           