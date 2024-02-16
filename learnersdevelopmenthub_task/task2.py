#  Unleash the Word Combinations Magic!
arr = ['a', 'b', 'c']

for i in arr:
    print(i)
    for j in arr:
        if i != j:
            print(i + j)
            for k in arr:
                if i != j and i != k and j != k:
                    print(i + j + k)