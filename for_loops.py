# for_loops.py


fruits = ['apple','banana','oranges']

# automatic index in python in for loops, not separately to be configured
for i in fruits:
    print(i)

# which position is which fruit? -->enumerate function
for k, i in enumerate(fruits):
    print(k, i)
