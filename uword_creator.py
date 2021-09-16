import random
def create(w):
    rn=random.randint(1,int(len(w)/2))
    uwl=[]
    rp=[]
    for i in range(rn):
        rp.append(random.randint(0,len(w)-1))
    for i in range(len(w)):
        if i in rp:
            uwl.append(w[i])
            uwl.append(" ")
        else:
            uwl.append('_')
            uwl.append(' ')
    uw="".join(uwl)
    ep=[i for i in range(len(uw)) if uw[i]=="_"]
    cw={}
    for i in ep:
        cw[i]=w[int(i/2)]
    return uw,cw