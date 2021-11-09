def sorter(to_sort: str) -> str:
    words=to_sort.split(" ")
    words.sort(key=str.casefold)
    sorted_words= " ".join(words)
    return print(sorted_words)



            
            
            