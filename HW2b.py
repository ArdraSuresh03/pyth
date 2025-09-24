
grocery_list = ["milk", "bread", "eggs"]



def add_item(item):
    grocery_list.append(item)   



def remove_last_item():
    if grocery_list:           
        grocery_list.pop()      
    else:
        print("The list is already empty!")



display = lambda items: [print("Item:", i) for i in items]



def count_characters(items):
    if not items:                  
        return 0                   
    return len(items[0]) + count_characters(items[1:])
    



print("Initial List:", grocery_list)     

add_item("butter")                       
print("After adding butter:", grocery_list)

remove_last_item()                       
print("After removing last item:", grocery_list)

print("\n--- Displaying items using lambda ---")
display(grocery_list)                   

print("\nTotal characters in all items:", count_characters(grocery_list))
