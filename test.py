a = [2,4,3,5,2,1,3,]
seen = []


for i in a:
    if i not in seen:
        seen.append(i)
    

print(seen)