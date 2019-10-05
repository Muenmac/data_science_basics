# operators.py


x = 5
y = 7

# arithemtic operators
z = x + y
print(z, type(z))

z = x - y
print(z)
z = x * y
print(z)
z = x / y
print(z)

# % modulo operator for the rest of 2 variables, NOT the actual result

z = x % y
print(z)

# exponential, 5^7

z = x ** y
print(z)

# NOR division, Doppelteilen, Ergebnis ist nach unten abgerundeter Wert

z = x // y
print(z) # wird nicht 0,71 sondern 0, da nach unten abgerundet

# Zuweisungsoperatoren, assignment operators
a = 3
a += 3
a -= 8
a *= 3
a /= 3
print(a, type(a)) # by dividing, variable ist casted from int to float


# Vergleichsoperatoren
d = 5
e = 6

print(d==e)
print(d!=e)
print(d>e)
print(d<e)
print(d<=e)

# logische Operatoren, mehrere Bedingungen miteinander verknüpfen

print(d < y and d ==e)
print(d < y or d ==e)




