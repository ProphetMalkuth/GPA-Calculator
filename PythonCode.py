print("GPA calculator")

print("="*30)

subjects=["ฟิสิกส์","เคมี","ชีวะ","คณิตศาสตร์","ภาษาอังกฤษ","ภาษาไทย","สังคมศึกษา"]
credit=[2.0,1.5,1.5,1.5,1.0,1.0,1.0]
i=-1
score={}
error=0
b={}
total=0

for x in subjects:
     score[x]=float(input(f"คะแนนวิชา{x}:"))
#{'ฟิสิกส์': 24.0, 'เคมี': 56.0, 'ชีวะ': 32.0, 'คณิตศาสตร์': 66.0, 'ภาษาอังกฤษ': 5.0, 'ภาษาไทย': 32.0, 'สังคมศึกษา': 45.0}
print("="*30)

#score[n] = คะแนน, score = ชื่อวิชา:คะแนน, n = ชื่อวิชา

for n in score: 
    if score[n]<0 or score[n]>100:
        print(f"คะแนนวิชา{n}ของคุณไม่ถูกต้อง")
        error=1
    else:
        if(score[n]>=80):
            i+=1
            print(f"วิชา{n} หน่วยกิต {credit[i]} เกรด 4") #{4*credit[i]} ค่าคะแนนที่เก็บไว้
            b[n]=4*credit[i]
        elif(score[n]>=75):
            i+=1
            print(f"วิชา{n} หน่วยกิต {credit[i]} เกรด 3.5")
            b[n]=3.5*credit[i]
        elif  (score[n]>=70):
            i+=1
            print(f"วิชา{n} หน่วยกิต {credit[i]} เกรด 3.0")
            b[n]=3*credit[i]
        elif  (score[n]>=65):
            i+=1
            print(f"วิชา{n} หน่วยกิต {credit[i]} เกรด 2.5")
            b[n]=2.5*credit[i]
        elif  (score[n]>=60):
            i+=1
            print(f"วิชา{n} หน่วยกิต {credit[i]} เกรด 2.0")
            b[n]=2*credit[i]
        elif  (score[n]>=55):
            i+=1
            print(f"วิชา{n} หน่วยกิต {credit[i]} เกรด 1.5")
            b[n]=1.5*credit[i]
        elif  (score[n]>=50):
            i+=1
            print(f"วิชา{n} หน่วยกิต {credit[i]} เกรด 1.0")
            b[n]=1*credit[i]
        else:
            i+=1
            print(f"วิชา{n} หน่วยกิต {credit[i]} เกรด 0")
            b[n]=0*credit[i]

print("="*30)

if error==0:
    for m in b:
        total+=b[m]
    f=total/9.5
    print("หน่วยกิตรวมคือ 9.5")
    print("เกรดเฉลี่ยของคุณคือ %.2f"%f)
else:
    print("ไม่สามารถคำนวนหน่วยเกรดเฉลี่ยได้")
