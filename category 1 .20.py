      #simple intrest
p=int(input("Enter the Principle amount:"))
n=int(input("Enter the number of years:"))
SC=input("Senior Citizen Yes/No:")
G=input("Male/Female:")
if SC=='Y' and G=='M':
    print("SI=",(p*n*12)/100)
elif SC=='Y' and G=='F':
    print("SI=",(p*n*15)/100)
else:
    print("SI=",(p*n*10)/100)
              #factors of x
x=int(input("Enter the number:"))
y=[]
print("The factors of",x,"are:")
for i in range(1, x):
    if x % i == 0:
        y.append(i)
print(y)
print("Number of factors:", len(y))
n=int(input("Enter N value:"))
if n>len(y):
    print("Invalid")
else:
    print("First", n, "factors:")
    for k in range(0,n):
        print(y[k], end=' ')
        #nth factor
x=int(input("Enter the number:"))
y=[]
print("The factors of",x,"are:")
for i in range(1, x + 1):
    if x % i == 0:
        y.append(i)
print(y)
print("Number of factors:", len(y))
n=int(input("Enter N value:"))
print(n, "th factor is:",y[n-1])
        #unique permutations
import itertools
n=input("Enter the number")
P=list(itertools.permutations(n))
print(*[''.join(p) for p in P])
       #sqaure and cubic numbers
import math
num=float(input("Enter the number:"))
print("Square number=",math.pow(num,2))
print("Cube number=",round(math.pow(num,3),3))
          #binary to decimal,decimal to octal
num=input("Enter the binary number:")
bin_num="01"
for i in range(len(num)):
    binary=True
    if num[i] not in bin_num:
        print("Invalid input")
        binary=False
        break
if binary:
    dec_number=int(num,2)
    oct_number=oct(dec_number)
    hexa=hex(dec_number)
    print("Decimal Equivalent=",dec_number)
    print("Octal Equivalent=",oct_number)
    print("Hexa Equivalent=",hexa)
           #add binary
num1=input("Enter the binary number 1=")
num2=input("Enter the binary number 2=")
sum=bin(int(num1,2)+int(num2,2))
print("Sum of binary numbers: ",sum[2:])
# greastest number in binary
a='1101'
b='1110'
c='1111'

bina=int(a,2)
binb=int(b,2)
binc=int(c,2)

if bina>binb and bina>binc:
    print("Greatest is", a)
elif binb>bina and binb>binc:
    print("Greatest is", b)
else:
    print("Greatest is", c)
    #greatest numbers wiyh initalize
 
bina=int(input("enter the number" ))
binb=int(input("enter the number"))
binc=int(input("enter the number"))

if bina>binb and bina>binc:
    print("Greatest is",bina)
elif binb>bina and binb>binc:
    print("Greatest is",binb)
else:
    print("Greatest is",binc)
    #multiplication of matrix
X=[[1,2],
   [5,3]]
Y=[[2,3],
   [4,1]]
result=[[0,0],[0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)




