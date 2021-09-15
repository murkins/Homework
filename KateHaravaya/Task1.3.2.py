""" Task 1.3. Create a program that asks the user for a number
 and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number."""

def task_1_3_2(number):
    res_num = []
    for divisor in range(1, number+1, 1):
        if number % divisor == 0:
            res_num.append(divisor)
    return res_num

print(task_1_3_2(60))
