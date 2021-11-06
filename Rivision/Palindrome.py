#Reverse the String
#Check reversed string is palindrome or not


value = input("Enter the String:")
reverse = (value[::-1])
if reverse == value:
    print('String is Palindrome')
else:
    print('Not palindrome')
