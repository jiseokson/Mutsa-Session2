for i in range(100): # for (변수) in (이터러블)
    print(i)

sum = 0
for i in range(1, 100 + 1):
    sum = sum + i
print(sum)

progress = 0
while progress < 100:
    progress = progress + 1
    print(f"{progress}% completed..")


while True:
    code = input('>>> ')
    if (code == 'exit'):
        break