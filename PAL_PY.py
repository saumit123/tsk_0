
test_cases = int(input())

for k in range(0,test_cases):
    s = input()
    s = s.lower()
    y=""
    for i in range(0,len(s)):
        y+=s[len(s)-i-1]
    if(y==s):
        print('It is a palindrome')
    else:
        print('It is not a palindrome')

