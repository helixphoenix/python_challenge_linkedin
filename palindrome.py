import re
def palindrome (pal: str) -> bool:
    pal_valid=re.sub('[^a-zA-Z]',"",pal )
    is_pal=pal_valid.lower()
    N= len(is_pal)
    for i in range(N):
        if is_pal[i]!=is_pal[N-i-1]:
            return False
    return True

