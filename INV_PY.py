
def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
        print(f"UPDATED Item {item_name}")
    else:
        inventory[item_name] = quantity
        print(f"ADDED Item {item_name}")


def delete_item(inventory, item_name, quantity):
    if item_name not in inventory:
        print(f"Item {item_name} does not exist")
    else:
        if inventory[item_name] < quantity:
            print(f"Item {item_name} could not be DELETED")
        else:
            inventory[item_name] -= quantity
            print(f"DELETED Item {item_name}")


def calculate_total_quantity(inventory):
    total_quantity = sum(inventory.values())
    print("Total Items in Inventory:")
    print(total_quantity)


def main():
    T = int(input())  

    for _ in range(T):
        N = int(input())  
        inventory = {}  

        
        for _ in range(N):
            item_name, item_quantity = input().split()
            inventory[item_name] = int(item_quantity)

        M = int(input()) 

        
        for _ in range(M):
            operation, item_name, quantity = input().split()
            quantity = int(quantity)
            
            if operation == "ADD":
                add_item(inventory, item_name, quantity)
            elif operation == "DELETE":
                delete_item(inventory, item_name, quantity)

        calculate_total_quantity(inventory)

if __name__ == "__main__":
    main()
