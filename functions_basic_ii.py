# 1. Countdown
def countdown(num):
    return list(range(num, -1, -1)) #This line creates a list that counts down from num to 0 using the range() function, and then converts it into a list using list().

print("Countdown:", countdown(5))  


# 2 print and return
def print_and_return(lst):
    print(lst[0])
    return lst[1]

result = print_and_return([1, 2])  
print("Return value:", result)


# 3. First Plus Length
def first_plus_length(lst):
    return lst[0] + len(lst)

print("First plus length:", first_plus_length([1, 2, 3, 4, 5])) 


# 4. Values Greater than Second
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    second_item = lst[1]
    lst2 = []
    for x in lst:
        if x > second_item:
            lst2.append(x)
    
    print(len(lst2))
    return lst2

print( values_greater_than_second([5, 2, 3, 2, 1, 4])) 
print( values_greater_than_second([3]))  


# 5. This Length, That Value
def length_and_value(size, value):
    return [value] * size

print( length_and_value(4, 7)) 
print(length_and_value(6, 2)) 
