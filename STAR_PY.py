
test_cases = int(input())

for k in range(0,test_cases):
    num = int(input())

    for i in range(0,num+1):
        c=0
        for j in range(num,i,-1):

            #print('*',end="")
            #c+=1
            if(c>3):
                print('#',end='')
                c=0
            else:
                print('*',end='')
                c+=1
        print()



