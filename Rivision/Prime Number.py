# to find out the Prime Number in Python

#Simple Take 1 Number and dived by 2 if answer is 0 it is not prime
# if Answer is not 0 Number is Prime

# num = 17
# if num > 0:
Number = int(input("Enter your Number:"))
if Number > 0:
    for i in range(2 , Number):
        if (Number % i) == 0:
            print(Number ,"is not Prime Number")
            break
else:
    print(Number,"is Prime Number")

