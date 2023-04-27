tup = (1, 2, 3)
print(tup)
print(tup[0])

# tup[0] = 1 # tupple은 immuttable

for i in tup:
    print(i)

list_1 = list(tup) # list로 형변환
list_2 = [i for i in tup] # comprehension
list_3 = []
for i in tup:
    list_3.append(i)
print(list_1)
print(list_2)
print(list_3)