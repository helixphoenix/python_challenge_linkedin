import requests

from pathlib import Path

def find_sequencing_name(file_url):
    url_parts=file_url.split("/")
    return url_parts[-1]

def find_sequence_index(file_name):
    digit_indexes=[]
    for i in range(len(file_name)):
        if file_name[i].isdigit():
            digit_indexes.append(i)
    return digit_indexes        
        
        
def increase_sequence(file_sequence):
    s=len(file_sequence)
    increase=int(file_sequence)+1
    increased_seq=str(increase)     
    l=len(increased_seq)
    inc_sequence=f"{file_sequence[:s-l]}{increased_seq}"
    return inc_sequence

    

def downloander(file_url,output_path):
    Path(output_path).mkdir(exist_ok=True)

    file_name=find_sequencing_name(file_url)
    n=len(file_name)
    m=len(file_url)
    digits=find_sequence_index(file_name)
    file_sequence=file_name[digits[0]:digits[-1]+1]


    while requests.get(file_url).status_code==200:
        file=requests.get(file_url)
        file_path=f"{output_path}/{file_name}"
        print(file_path)
        open(file_path,"wb").write(file.content)
        file_sequence=increase_sequence(file_sequence)
        print(file_sequence)
        file_name=f"{file_name[:digits[0]]}{file_sequence}{file_name[digits[-1]+1:]}"
        file_url=f"{file_url[:m-n]}{file_name}"
        
    
    



downloander('https://699340.youcanlearnit.net/image001.jpg','path/resimler')
    