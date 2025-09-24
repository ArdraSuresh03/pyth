fruits=["apple", "banana", "cherry"]
vegetables=["carrot", "broccoli", "spinach"]
beverages=["water", "juice", "soda"]


fruits.append("orange")

vegetables.insert(1,"Tomato")
                  
beverages.pop()   

inventory=[fruits,vegetables,beverages]
print(inventory)

print("first two fruits:",fruits[:2])

print("last vegetable:",vegetables[-1])

fruits_length=[len(x)for x in fruits]
print("length of  fruit name:",fruits_length)

print("is 'water' in beverages?","water" in beverages)

tuple_first_items=(fruits[0],vegetables[0],beverages[0])
print("Tuple of first items:",tuple_first_items)