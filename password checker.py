#Check password (Strong or Medium or week or very week)
#Upper case, lower case, digit and special chracters is a strong password!

pas = input("Please enter password: ")
L=0
U=0
D=0
S=0

for x in pas:
    if x.islower():
        L1=1
    elif x.isupper():
        U=1
    elif x.isdigit():
        D=1
    else:
        S=1

sum = L+U+D+S

if sum == 4:
    print ("Strong!")
elif sum == 3:
    print ("Medium")
elif sum == 2:
    print ("Week")
else:
    print ("Very week")
