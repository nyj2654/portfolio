print('성학고등학교 1학년 1반 2학기 학생성적 입력')
print('=================================================')

students = {} #빈 딕셔너리 생성

#get_grade 함수는 주어진 점수에 대한 학점을 계산
def get_grade(score):
    if score >= 95:
        return 'A+'
    elif score >= 90:
        return 'A0'
    elif score >= 85:
        return 'B+'
    elif score >= 80:
        return 'B0'
    elif score >= 75:
        return 'C+'
    elif score >= 70:
        return 'C0'
    elif score >= 60:
        return 'D0'
    else:
        return 'F0'

def add_student(): 
    name = input('이름 : ') 
    scores = [] 
    subjects = ['국어', '영어', '수학'] 
    for subject in subjects: 
        score = int(input(f'{subject} 점수 : '))
        scores.append(score) 
    students[name] = scores 

while True: #while 루프를 사용해서 학생 정보를 계속 입력받음
    add_student() 
    qu = input('다른 학생의 정보를 추가 하시겠습니까?(y/n): ') 
    if qu.lower() != 'y': 
        break

count = len(students) #students 딕셔너리의 학생 수를 계산하여 count 변수에 저장

#students 딕셔너리를 순회하며 각 학생의 점수를 합산하여 총점 계산 후 totals 딕셔너리에 저장
totals = {student: sum(scores) for student, scores in students.items()} #item - 튜플(여러 개의 값을 저장할 수 있는 컨테이너)을 가리키는 변
#students 딕셔너리를 순회하며 각 학생의 점수를 합산하고, 점수의 개수를 나누어 평균 계산 후 avgs 딕셔너리에 저장
avgs = {student: sum(scores) // len(scores) for student, scores in students.items()}
#각 학생의 평균 점수를 기반으로 학점 할당 - avg 딕셔너리를 순회 후 각 학생과 평균 점수에 대해 get_grade 함수를 호출하여 학점을 결정 후 학점 결과를 grade 딕셔너리에 저장
grades = {student: get_grade(avg) for student, avg in avgs.items()}

#각 과목의 총점을 계산 - index(0,1,2)를 순회하며 과목을 나타내고, 각 index에 대해 학생들의 i번째 점수를 합산하여 총점 계산(결과 리스트에는 각 과목의 총점이 저장)
subject_totals = [sum(scores[i] for scores in students.values()) for i in range(3)]
#각 과목의 평균 점수 계산 - subject_totals 리스트를 순회하고, 각 총점에 대해 학생 수로 나우어 평균을 계산하고 결과를 subject_avgs 리스트에 저장
subject_avgs = [total // count for total in subject_totals]

print('=================================================')
print('성한고등학교 1학년 1반 이번학기 성적 현황')
print(f"총 학생 수 : {count}명")
print('=============================================================')
print("순번\t이름\t국어\t영어\t수학\t총점\t평균\t학점")
print('=============================================================')

for idx, (name, scores) in enumerate(students.items(), start=1):
    total = totals[name]
    avg = avgs[name]
    grade = grades[name]
    print(f"{idx}\t{name}\t{scores[0]}\t{scores[1]}\t{scores[2]}\t{total}\t{avg}\t{grade}")

print('==============================================================')
print(f"과목 총점:\t{subject_totals[0]}\t{subject_totals[1]}\t{subject_totals[2]}")
print(f"과목 평균:\t{subject_avgs[0]}\t{subject_avgs[1]}\t{subject_avgs[2]}")
