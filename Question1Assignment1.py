# Question 1

threshold = 100
product = 1
currentNumber = 1

while product <= threshold:
    product = product * currentNumber
    if product > threshold:
        break

    currentNumber = currentNumber + 1
print("The final product is", product)
print("The integer that caused the product to exceed the threshold is", currentNumber)