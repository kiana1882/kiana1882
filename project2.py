numbers=[12, 75, 150, 180 , 145, 525 , 50]
c=sorted(numbers)
d=[]
print(c)
for i in c:
            if  i==150:
                continue
            if i>=500:
                break
            if i%5==0:
              d.append(i)
print(d)
