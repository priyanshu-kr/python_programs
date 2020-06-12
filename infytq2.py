def fun(str):
    l=list(str)
    l1=[]
    l2=[]
    c=0
    for i in l:
        if i>=chr(48) and i<=chr(57):
            l1.append(i)
    for i in l1:
        if i not in l2:
            l2.append(i)        
    for i in l2:
        if int(i)%2==0:
            c=1
            break
    if c==0:
        return -1
    else:
        l2.sort()
        l2.reverse()
    n=len(l2)
    for i in range(n-1,-1,-1):
        if int(l2[i])%2==0:
            a=l2[i]

            l2.pop(i)
            break
    l2.append(a)
    string=""
    for i in l2:
        string=string+i
    return int(string)
            

    
    
     
