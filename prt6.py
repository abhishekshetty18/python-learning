my_fruits = {"apple", "mango", "cherry", "papaya"}
friend_fruit = {"apple", "banana", "orange","kiwi"}
print("union: ",my_fruits | friend_fruit)
print("intersection: ",my_fruits & friend_fruit)
print("difference: ", my_fruits - friend_fruit)
my_fruits.add("grapes")
print(my_fruits)
my_fruits.remove("papaya")
print(my_fruits)
my_fruits.discard("mango")
print(my_fruits)