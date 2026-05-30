print("GPA Calculator")

print("="*30)

subjects={
    "ฟิสิกส์":2.0,
    "เคมี":1.5,
    "ชีวะ":1.5,
    "คณิตศาสตร์":1.5,
    "ภาษาอังกฤษ":1.0,
    "ภาษาไทย":1.0,
    "สังคมศึกษา":1.0
}
grade={
    80:4.0,
    75:3.5,
    70:3.0,
    65:2.5,
    60:2.0,
    55:1.5,
    50:1.0,
}
b={}
score={}

for item in subjects.keys():
    score[item]=float(input(f"คะแนนวิชา{item}: "))

print("="*30)

for n in score.keys():
    if score[n]<0 or score[n]>100:
        print(f"คะแนนวิชา{n}ของคุณไม่ถูกต้อง")
        error=1
    else:
        for key in grade.keys():
            print(1)