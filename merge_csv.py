import pandas as pd



def csv_merger(csv_files):

    merged_csv=pd.DataFrame()
    for file in csv_files:
        file_read=pd.read_csv(file)
        print("filecontent:",file_read)
        merged_csv=pd.concat([file_read,merged_csv],axis=0, ignore_index=True)
    return merged_csv.to_csv('merged.csv')    
        



csv_merger(['addresses.csv','airtravel.csv'])
        
        

        
        
        
    

    
    
    
    
    