
test_cases = int(input())

items = []
qty = []
def formula(func,name,quantity):
    if (name not in items) and func=='ADD':
        items.append(itm)
        qty.append(quantity)
        print('Added Item '+name)
    elif (name in items) and func=='ADD':

        qty[items.index(itm)] += qt
        print('Added Item '+name)

    elif(name in items)and func=='DELETE':
        if(qty[items.index(name)] >= quantity):
            qty[items.index(name)]-=quantity
            print('Deleted Item '+name)
        else:
            print('Item '+name+' could not be DELETED')


for k in range(0,test_cases):
    n = int(input())
    for j in range(0,n):
        itm,qt = input().split(' ')
        qt = int(qt)
        items.append(itm)
        qty.append(qt)
        #items.append(itms)


    fun = int(input())
    for i in range(0,fun):
        function,names,quantit = input().split(' ')
        quantit = int(quantit)
        formula(function,names,quantit)



sum = 0
for quantities  in qty:
    sum+=quantities
print('Total Items in Inventory:',end=' ')
print(sum)



