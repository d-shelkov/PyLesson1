RunAgain = True
second = False
num3d = '0'
while RunAgain:
    if second: print("You need to enter a positive three-digit number.. Please be attentive")
    num3d = input("Please enter three digit positive number: ")
    if num3d.isdigit(): 
        RunAgain = False if 99 < int(num3d) < 1000 else True
    second = True
print('Digits of entered number are: ', num3d[0], ', ', num3d[1], ' and ', num3d[2], '.')
print('Sum of number digits is: ', int(num3d[0]) + int(num3d[1]) + int(num3d[2]))
