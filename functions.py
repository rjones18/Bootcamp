# Part 1
def double(my_number):
    numbers = (2*my_number)
    return numbers

print(double(2))
print(double(4))
print(double(10))


# Part 2
def negative(num):
    if num >= 0:
        return False
    else:
        return True
    
print(negative(5))
print(negative(-1))
print(negative(0))
print(negative(0.0))


# Part 3 
def characters(go):
    if len(go)< 8:
        return False
    else:
        return True
    
first = characters('pizza') #I was hungry when thinking of words to put in this 
print(f'The answer is {first}')

second = characters
second = characters('tacobell')
print(f'The answer is {second}')


distance = float(input())

ask_for_distance('Peter')
ask_for_minutes("Peter",1000.0)
ask_for_distance('Jane')
ask_for_minutes("Jane",2000.0)
