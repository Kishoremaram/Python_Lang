str1=input("Enter string: ")
def palindrome(str1):
    if str1 == str1[::-1]:
        print("This is palindrome")
    else:
        print("This is not palindrome")
palindrome(str1)


str1=input("Enter string: ")
def palindrome(str1):
    count = 0
    j=-1
    for x in range(len(str1)):
        if str1[x] == str1[j]:
            count = count+1
            j=j-1
    if count==len(str1):
        print("This is palindrome")
    else:
        print("This is not palindrome")
palindrome(str1)
