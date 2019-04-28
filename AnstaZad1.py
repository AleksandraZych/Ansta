c="79-900"
b="80-155"
def change(a):
    a.split()
    s=[]
    for i in a:
        try: 
            int(i)
            s.append(int(i))
        except:
            continue
    iterator=1
    number=0
    for i in reversed( range(len(s))):
        number+=s[i]*iterator
        iterator=iterator*10
    return number
    
def code(start,stop):
    start=change(c)
    stop=change(b)
    result=[]
    for i in range(start, stop, 1):
        result.append(i)
    return result