# while.py


# as long as condition is fulfilled

a = 1
halt = False

while a < 10 and halt == False:
    print(a)
    if a == 5 or a == 2:
        halt = True
    a += 1

# conditions are linked with each other