inp=[1,2,3,4,5]

def check(n,inp):
    ori=[]
    for i in range (1,n+1):
        ori.append(i)
        
    missing=[]
    for i in range (1,n+1):
        missing.append(i)
    
    for o in ori:
        if o in inp:
            missing.remove(o)
    return missing
