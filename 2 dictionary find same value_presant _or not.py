x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
for i,j in y.items():
    if  x[i]==y[i]:
        print(i,'.',j,'presant in x,y both' )