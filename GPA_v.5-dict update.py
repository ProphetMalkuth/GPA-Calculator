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
    50:1.0
}
b={}
score={}
error=0
total=0

for item in subjects.keys():
    score[item]=float(input(f"คะแนนวิชา{item}: "))

print("="*30)

for n in score.keys():
    if score[n]<0 or score[n]>100:
        print(f"คะแนนวิชา{n}ของคุณไม่ถูกต้อง")
        error=1
    else:
        for g in range(0,len(subjects)):
            if score[n]>=list(grade.keys())[g]:
                print(f"วิชา{n} หน่วยกิต {subjects[n]} เกรด {list(grade.values())[g]}")
                b[n]=(subjects[n])*(list(grade.values())[g])
                break
            if(score[n]<50):
                print(f"วิชา{n} หน่วยกิต {subjects[n]} เกรด 0")
                b[n]=0
                break

print("="*30)

if error==0:
    for m in b:
        total+=b[m]
    f=total/sum(subjects.values())
    print(f"หน่วยกิตรวมคือ {sum(subjects.values())}")
    print("เกรดเฉลี่ยของคุณคือ %.2f"%f)
else:
    print("ไม่สามารถคำนวนหน่วยเกรดเฉลี่ยได้")