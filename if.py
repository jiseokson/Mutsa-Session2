value = int(input('값을 입력해주세요: '))

if value > 10:
    print('10보다 크다')
else:
    print('10보다 작거나 같다')

score = int(input('점수를 입력하세요: '))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')