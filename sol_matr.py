
matr = [ [4,6,1,0], [12,42,17,21],
         [3,9,2,6], [25,18,10,13] ]
n = len(matr)
for item in matr: print(item)

for item in matr: 
    if len(item)!=n: break
else: 
    print(f'{n}*{n}')
    list = []
    for i in range(0,n) : 
        list.append(matr[i][i])
    print(list)
