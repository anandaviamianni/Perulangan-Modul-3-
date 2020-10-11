for i in range(5):
    for j in range(i,5):
        print("*",end = "")
    print("")
print("\n")

a = 6 
for i in range(0,6):
    for j in range(0,i+1):
            print("*",end = "")
    print("")
print("\n")

a = 6
for i in range(0,a):
    for j in range(0,a-1):
        print("*",end = "")
    a -= 1
    print("")
print("\n")

a = 5 
s = 2*a - 2
for i in range(0,a):
    for j in range(0,s):
        print("*",end= "")
    s -= 2
    for j in range(0,i+1):
        print("*",end = "")
    print("")