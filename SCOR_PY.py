if __name__ == '__main__':
    
    for i in range(int(input())):
        n = int(input())
        list = []
        for s in range(n):
            name, marks = input().split()
            list.append([float(marks),name])
            list.sort()
            
        l = len(list)
        top = []
        for p in range(len(list)):    
            top.append(list[l-p-1][1])
            if p !=len(list)-1 and list[l-p-1][0] != list[l-p-2][0]:
                break
        top.sort()
        for t in range(len(top)):
            print(top[t])