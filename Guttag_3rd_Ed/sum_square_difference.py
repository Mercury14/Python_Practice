def sum_squares(number):
    total = 0
    for x in range (1, number+1):
        total = total + (x**2)
    return total

def square_sum(number):
    total = 0
    for x in range (1, number+1):
        total = total + x
    return total **2



print(square_sum(100)- sum_squares(100))