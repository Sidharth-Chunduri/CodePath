#

def squared(numbers):
    output = []
    for number in numbers:
        output.append(number ** 2)
    
    print(output)


numbers = [1, 2, 3]
squared(numbers)