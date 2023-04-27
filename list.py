mbti = ['INFJ', 'ESTJ', 'ENFP']
print(mbti[0]) # 원소 접근

my_list = [123, 'apple']
print(my_list)

colors = ['red', 'blue', 'green']
colors.append('purple') # 뒤에 추가
print(colors)

colors.insert(1, 'yellow') # 중간에 삽입
print(colors)

del colors[0] # 임의 위치 삭제
print(colors)

c = colors.pop() # pop 연산
print(colors)
print(c)

numbers = [2, 6, 4, 2, 2, 8, 9, 0, 12]
print(sorted(numbers)) # 정렬된 객체를 반환
print(numbers)
numbers.sort() # 객체 자체를 정렬
print(numbers)

colors = ['red', 'blue', 'green', 'orange', 'yellow']
print(colors)
print(colors[1:2]) # 1 <= i < 2인 elements
print(colors[::-1])

scores = [100, 80, 76, 45, 0, 23, 88, 97]
scores.sort(reverse=True)
for i in scores:
    if i >= 80:
        print(i)
    else:
        print('FAIL')

score_max = max(scores) # 최대값
score_min = min(scores) # 최소값
score_sum = sum(scores) # 총합
print(f'mean is {score_sum / len(scores)}')
