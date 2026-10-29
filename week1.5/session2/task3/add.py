# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum

from money import Money

m1 = Money(100,67)
m2 = Money(5,39)
m = m1 + m2
print(f"{m1} + {m2} = {m}")