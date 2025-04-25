
# ----- Positive and Negative Exponents -----
print(10**1)
print(10**2)
print(10**3)

print(10**0)

print(10**-1)
print(10**-2)
print(10**-3)


# ----- User Input = String -----
text = input("Enter a number")
print(text)

print(len(text))

# error - can't do math here
# print(text+3)

# ----- Cast input as a float or int variable -----
text = input("Enter a number")
num = float(text)
print(num + 4)


# ----- Now put it all together -----
# Get string input, which will include a decimal point
digits = input("Enter a decimal number to convert: ")

# Get number of decimal places as an integer
exponent = int(len(digits))-1

# Convert the input to a float number
n = float(digits)

# Use the exponent to get the numerator
numerator = int(n * 10**exponent)

# Use the expoent to get the denominator
denominator = 10**exponent

# percent is the first two decimal places
percent = n * 100

# Output
print("The decimal is ", n)
print("The fraction is ", numerator, "/", denominator)
print("The percent is ", percent, " %")









"""
