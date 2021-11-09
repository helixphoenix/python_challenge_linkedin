


from zipfile import ZipFile
import glob, os

def extention_searcher(files_directory,file_extentions):
    files_to_zip=[]
    for extention in file_extentions:
        pather=f"{files_directory}/*.{extention}"
        for file in glob.glob(pather):
            files_to_zip.append(file)
    
    return files_to_zip
    

def zipper(files_directory,file_extentions,output_directory):
    output_path=f"{output_directory}/zipped.zip"
    zipped=ZipFile(output_path,'w')
    files=extention_searcher(files_directory,file_extentions)
    for file in files:
        zipped.write(file)
        
    return zipped    
    
    
    


zipper('pathtofiles',['csv','txt'],'outputpath')    
    
    

