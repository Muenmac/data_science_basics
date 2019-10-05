# strings.py


a = "Hello World"
b = 'Hello World'

# access some specific letter, equal to access an index
print(a[0])

# access a range [x:y], start with x and end before y
print(b[2:7])

# access length and print onl upper cases
print(len(a), a.upper())

# split a string
print(a.split(" "))

x = a.split(" ")
print(x[1])

c = a + " " + b
print(c)