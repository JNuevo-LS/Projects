def fibonacci_generator(number):
    fibonacci_list = []
    count = 0
    while count < number - 1:
        if count == 0:
            fibonacci_list.append(1)
            count += 1
        if count == 1:
            fibonacci_list.append(1 + fibonacci_list[0])
            count += 1
        if count > 1:
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
            count += 1
    print(fibonacci_list[-1])
fibonacci_generator(number = 14)