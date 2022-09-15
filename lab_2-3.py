a = 2
print (a)
print (type(a))
a = float(a)
print (type(a))
print (a)
a = str(a)
print (type(a))
a = bool(a)
print (type(a))
print (a == 2)
# The result is false bcause after changing a = 2 to a float, it changed to a = 2.0 which results in 2 not being equal to 2.0 with the boolean