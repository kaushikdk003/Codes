def multiple_of_3_5():
    sum = 0
    for i in range(1, 100):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    return sum


print("The sum of numbers that are 3&5 multiples below 100 are")
print(multiple_of_3_5())
