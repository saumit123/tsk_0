def slice_operation(list):   
    
    for i in range(len(list)):
        print(list[::-1][i], end=" ")

        if i == len(list)-1:
            print(end="\n")
        
    for i in range(len(list[3::3])):
        print(list[3::3][i]+3, end=" ")
        if i == len(list[3::3])-1:
            print(end="\n")

    for i in range(len(list[5::5])):
        print(list[5::5][i]-7, end=" ")
        if i == len(list[5::5])-1:
            print(end="\n")    
        
    sum  = 0

    for i in range(5):
        sum = sum + list[3:8:][i]
    
    print(sum)

if __name__ == '__main__':
    
    for i in range(int(input())):
        l = int(input())
        list = list(map(int,input().split()))
        
        slice_operation(list)