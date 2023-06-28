RunAgain = True
second = False
num3d = '0'
while RunAgain:
    if second: print("You need to enter a positive three-digit number.. Please be attentive")
    num3d = input("Please enter three digit positive number: ")
    if num3d.isdigit(): 
        RunAgain = False if 99 < int(num3d) < 1000 else True
    second = True
d3 = int(num3d) - int(num3d) % 100
d2 = (int(num3d) - d3) - (int(num3d) - d3) % 10
d1 = int(num3d) % 10
print('Digits of entered number are: ', int(d3/100), ', ', int(d2/10), ' and ', d1, '.')
print('Sum of number digits is: ', int(d3/100) + int(d2/10) + d1)
