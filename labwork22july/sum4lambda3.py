def sum(a,b,c,d):
    return a+b+c+d


L1=[1,2,3]
L2=[4,5,6]
L3=[3,4,5]
L4=[2,6,7]

L_lam=[x for x in map(lambda a,b,c,d:a+b+c+d,L1,L2,L3,L4)]
print(L_lam)
