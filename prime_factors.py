from typing import List
def primer(source_number: int) -> List[int]:
    prime_numbers=[]
    base=2
    while base<=source_number:
        if source_number%base==0:
           prime_numbers.append(base)
           source_number=int(source_number/base)
        else:   
            base+=1
    return print(prime_numbers)
    
    
