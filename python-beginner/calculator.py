
# Create Simple Caluclatpr

def create_calculator(value1, value2, defaultOperation='add'):
    
    if defaultOperation == "add":
        return value1 + value2
    elif defaultOperation == 'sub':
        return value1 - value2
    elif defaultOperation == 'mul':
        return value1 * value2
    elif defaultOperation == 'div':
        return value1/value2

create_calculator(10,10)
print(create_calculator(10,10, 'add'))
print(create_calculator(10,10, 'sub'))
print(create_calculator(10,10, 'mul'))
print(create_calculator(10,10, 'div'))