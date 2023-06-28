RunAgain = True
second = False
ticketnum = '0' # Ticket number
while RunAgain:
    if second: print("You need to enter exactly a six digit positive ticket number. Please be attentive")
    ticketnum = input("Please enter a six digit positive ticket number: ")
    if ticketnum.isdigit(): 
        RunAgain = False if 99999 < int(ticketnum) < 1000000 else True
    second = True
if int(ticketnum[0])+int(ticketnum[1])+int(ticketnum[2]) == int(ticketnum[3])+int(ticketnum[4])+int(ticketnum[5]):
    print("Congratulations!!! You have lucky tycket.")
else: print("Unfortunatly you don't have lucky ticket now. Probably you will be lucky next time!")
