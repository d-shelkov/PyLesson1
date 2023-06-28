def intNumEnter(msg=''):
    numstr = '0'
    num = 0
    RunAgain = True
    while RunAgain:
        numstr = input(msg)
        if numstr.isdigit(): 
            num = int(numstr)
            RunAgain = False if num > 0 else True
    return num
ChocoW = 0 # Chocolate plate width in chunks
ChocoL = 0 # Chocolate plate length in chunks
ChunksNum = 0 # Chunks number to breake with
ChocoW = intNumEnter('Please enter chocolate plate width in chunks: ')
ChocoL = intNumEnter('Please enter chocolate plate length in chunks: ')
ChunksNum = intNumEnter('Please enter chunks amount to break with: ')
if (ChunksNum % ChocoL == 0 or ChunksNum % ChocoW == 0) and ChunksNum < ChocoW*ChocoL:
    print('Yes, it is possible to break chocolate plate with ', ChunksNum,' piece(s) chunk by a strait line')
else: print('No, it is not possible to break chocolate plate with ', ChunksNum,' piece(s) chunk by a strait line')