huruf = input().strip() 
awal = 'A'  

for i in range(ord(huruf) - ord(awal) + 1): 
    for j in range(i + 1):
        print(chr(ord(awal) + j), end=" ")  
    print() 
