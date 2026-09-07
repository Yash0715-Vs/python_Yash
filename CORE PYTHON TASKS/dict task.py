student={
's1':{
    'rollno':41,
    'name':"Yash",
    'marks':85,
    'grade':'none',
},
's2':{
    'rollno':42,
    'name':"Nimesh",
    'marks':90,
    'grade':'none',
},
's3':{
    'rollno':43,
    'name':"Aryan",
    'marks':75,
    'grade':'none',
},
's4':{
    'rollno':44,
    'name':"Sidharth",
    'marks':80,
    'grade':'none',
},
's5':{
    'rollno':45,
    'name':"Isha",
    'marks':85,
    'grade':'none',
}

}

for key in student:
    if student[key]['marks']>=90 and student[key]['marks']<=100:
        print(student[key]['grade'])

    elif student[key]['marks']>=80 and student[key]['marks']<90:
        print(student[key]['grade'])
    elif student[key]['marks']>=70 and student[key]['marks']<80:
        print(student[key]['grade'])
    elif student[key]['marks']>=60 and student[key]['marks']<70:
        print(student[key]['grade'])
    elif student[key]['marks']>=40 and student[key]['marks']<60:
        print(student[key]['grade'])
    else:
        print("Fail")

print("Student Information")
print(student)