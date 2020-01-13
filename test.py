import numpy as np
a = np.array([[" "]*80]*40)

for i in range(80):
    a[0][i] = 'X'
    a[29][i] = 'X'

print(a)

a[27][79] = 'z'

for i in range(30):
    for j in range(80):
        print(a[i][j],end = " ")

    print()
