RunAgain = True
second = False
papcrnum = '0'
while RunAgain:
    if second: print("You need to enter a positive six-digit number. Please be attentive")
    papcrnum = input("Please enter digit positive number: ")
    if papcrnum.isdigit(): 
        RunAgain = False if int(papcrnum) % 6 == 0 else True
    second = True
print('Digits of entered number are: ', num3d[0], ', ', num3d[1], ' and ', num3d[2], '.')
print('Sum of number digits is: ', int(num3d[0]) + int(num3d[1]) + int(num3d[2]))
