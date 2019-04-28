import re

c="79-900"
b="80-155"

def code(start,stop):
    start=re.sub('-','',c)
    stop=re.sub('-','',b)
    result=[]
    for i in range(start, stop, 1):
        result.append(i)
    return result
