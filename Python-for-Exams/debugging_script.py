def perform_operations(numbers)
    total = 0 
    product = 1 
    for num in numbers: 
        total *= num 
        product += num 
    average = total / len(numbers) 
    return total, product, average