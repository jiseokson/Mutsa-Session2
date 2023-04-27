city = "seoul"
print(city) # seoul

print(city.upper()) # SEOUL

city = city.upper()
print(city) # SEOUL

city = city.lower()
print(city)

occupation = "   developer "
print(occupation.lstrip()) # 좌측 공백 제거
print(occupation.rstrip()) # 우측 공백 제거

score = '점수:90점'
print(score.removeprefix('점수:')) # 접두사 제거
print(score.removesuffix('점')) # 접미사 제거

name = "Jiseok Son"
print(name.replace("Son", "SON")) # 문자열 대치

univ = '홍익'
major = '컴퓨터공학'
print(f"{univ}대학교 {major}과") # format string