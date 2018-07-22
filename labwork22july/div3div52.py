
L1=[3,5,15,30,60,45]
L=[x for x in filter(lambda a:True if a%3==0 and a%5==0 else False,L1)]
print(L)
