RunAgain = True
second = False
papcrnum = '0' # Paper crane(s) number
num = 0
while RunAgain:
    if second: print("You need to enter exactly a positive sixfold number. Please be attentive")
    papcrnum = input("Please enter a positive sixfold number: ")
    if papcrnum.isdigit(): 
        num = int(papcrnum)
        RunAgain = False if num % 6 == 0 and num > 0 else True
    second = True
print('Peter and Sergey made the ', int(num/6) ,' of paper crane(s) each. And Kate made ', int(num/6*4),' of paper crane(s).')
