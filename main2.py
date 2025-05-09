class Student:
    pass
    def __init__(self, a,b,c,):
        self.a = a
        self.b = b
        self.c = c

    def average(self):
        return(self.a+self.b+self.c)/3

n = int(input('학생 수 입력 (N): '))
for i in range(1, n+1, 1):
    a = int(input(f'{i}번째 학생의 국어 성적 입력: '))
    b = int(input(f'{i}번째 학생의 영어 성적 입력: '))
    c = int(input(f'{i}번째 학생의 수학 성적 입력: '))
    student = Student(a, b, c)
    print(f'{i}번째 학생의 평균: {student.average()}')