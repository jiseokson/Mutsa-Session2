with open('textfile.txt', 'a', encoding='UTF-8') as f:
    print(f.readlines()) # 라인들의 리스트를 반환
    f.write('새로운 텍스트가 추가되었습니다.')
    f.close()