
import re 
import random

def passphraser(num:int)->str:
    words=[]
    words_to_phrase=open("dicewarewordlist.txt", "r")
    lines=words_to_phrase.readlines()

    for line in lines:
        phrases=line.split("	")
        words.append(phrases[1].replace("\n",""))
    
    phrases=random.sample(words,num)
    
    passphrase="".join(phrases)
    print(passphrase)
    return passphrase
        
        
        


passphraser(16)    
    
    
    
    