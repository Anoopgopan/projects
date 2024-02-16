a = {100, 98, 101, ord('e'), 105}
b = list(a)
print(b)
for i in range(0,len(b)-1):  
    for j in range(len(b)-1):  
        if(b[j]>b[j+1]):   
            b[j],b[j+1] = b[j+1], b[j]  
print(b)

print("==========================================")
a = "Romantic"
print(a[::-1])
    

        

