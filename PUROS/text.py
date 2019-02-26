a = [1,1,1,2,3,3,3,3]
b = [1,2,3,4,5,6,7,9]

conjuntoa=set(a)
conjuntob=set(b)
c="conjuntoa {}-conjuntob {}".format(conjuntoa,b)
unionab = conjuntoa | conjuntob
interseccionab = conjuntoa & conjuntob
print(unionab)
print(interseccionab)
print(c)
print(2**3)