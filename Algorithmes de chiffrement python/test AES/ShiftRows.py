L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
M = []

i = 0
for j in range(int(len(L)/4)):
        M = M + L[(j*4+i):((j+1)*4)]
        M = M + L[(j*4):((j+1)*4)-4+i]
        i = i + 1
        if i == 4:
            i=0
            
print(M)
