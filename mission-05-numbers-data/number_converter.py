"""Convert a positive decimal integer to binary and hexadecimal."""

value = int(input("Enter a positive decimal number: "))
if value <= 0:
    raise SystemExit("Please enter a positive integer.")
print("Binary:", bin(value)[2:])
print("Hexadecimal:", hex(value)[2:].upper())
