

# 1. Basic - Print all integers from 0 to 150
for i in range(151):
    print(i)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1001, 5):
    print(i)

# 3. Counting, the Dojo Way - Print integers 1 to 100.
# If divisible by 5, print "Coding" instead.
# If divisible by 10, print "Coding Dojo"
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4/ Add odd integers from 0 to 500,000, and print the final sum.
sum_odd = 0
for i in range(1, 500000, 2):  # start at 1, step by 2 to get only odd numbers
    sum_odd += i
print("Sum of odd numbers from 0 to 500,000:", sum_odd)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    print(i)

# 6. Flexible Counter - Given lowNum, highNum, mult,
# print multiples of mult from lowNum to highNum
lowNum = 2
highNum = 9
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
