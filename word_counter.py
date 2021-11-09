
from collections import defaultdict
import operator


def count_words(path_to_file):
    words=defaultdict()
    file_to_read=open(path_to_file, "r")
    lines=file_to_read.readlines()
    
    for line in lines:
        read_words=line.split(" ")
        for word in read_words:
            if word in words:
               words[word]+=1
            else:
                words[word]=1    
    sorted_words=dict(sorted(words.items(),key=operator.itemgetter(1), reverse=True))     
    total_words= sum(sorted_words.values()) 

    
    message1=f" The total number of words are {total_words}, and the top 20 words are : "
    print(message1)
    for i in range(20):
        w=list(sorted_words.keys())[i]
        o=list(sorted_words.values())[i]
        print(f"'{w}' with {o} occurance")
        
        
        
        
count_words('words_to_count.txt')
    


     
            

                
            
    
    