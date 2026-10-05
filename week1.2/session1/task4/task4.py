# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
both = fruit.intersection(vegetables)
print("fruit.intersection(vegetables): ", both)

# Why does the following code diplay five items?
food = fruit.union(vegetables)
print("fruit.union(vegetables): ", food)

# Add an item to fruit
fruit.add("strawberry")

# Remove an item from vegetables
vegetables.discard("leek")

# Find and display symmetric difference of the two sets
print("fruit.symmetric_difference(vegetables): ", fruit.symmetric_difference(vegetables))
