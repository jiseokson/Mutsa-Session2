student = {
    "student_no": "C011103",
    "major": "Computer Science",
    "grade": 2,
}

print(student)
print(student['major']) # key 값으로 원소 접근

student["gpa"] = 4.5 # 추가
print(student)

student['major'] = 'Computer Engineering' # 수정
print(student)

del student['grade'] # 삭제

# 키가 존재하지 않을 때 리턴할 기본값을 설정할 수 있다
grade = student.get('grade', '해당 값이 존재하지 않습니다.')
print(grade)

print(student.keys()) # 키를 반환

print(student.values()) # 값을 반환

for i in student: # key를 순회
    print(i)

for key, value in student.items(): # key, value 쌍을 순회
    print(key, value)