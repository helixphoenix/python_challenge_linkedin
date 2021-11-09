import json
from pathlib import Path
def save_dic(dic)-> str:
    path= Path().absolute()
    file_name=f"{path}/previous_dics.json"
    with open(file_name, 'w+') as file:
        json.dump(dic,file)
    return file_name   
        


def load_dic(dic_path)-> dict: 
    with open(dic_path,'r') as dics:
        dictionaries=json.load(dics)
    return print(dictionaries )       
        
        
        
       
       
fitifiti= save_dic({"toproror":"ieioetuoew"})  

load_dic(fitifiti)  