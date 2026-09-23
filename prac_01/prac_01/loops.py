for i in range(1, 21, 2):
    print(i, end=' ')
print()

#Question a
for i in range(0, 100, 10):
    print(i, end=' ')
print()

#Question b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#Question c
number_of_stars = int(input("Enter number of stars: "))
for i in range(0, number_of_stars, 1):
    print("*", end=' ')
print()

#Question d
number_of_lines = int(input("Enter number of lines: "))
for i in range(1, number_of_lines + 1):
    print('*' * i)
