for x in range(0,151):
    print(x)

for x in range(5,1001):
    if x % 5 == 0:
        print(x)

for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")

sum = 0
for x in range(0,500001):
    if x % 2 != 0:
        sum= sum + x
print(sum)

for x in range(2018,0,-4):
    print(x)

lowNum=19
highNum=331
mult=6
for x in range(lowNum,highNum):
    if x % mult == 0:
        print(x)