student={
's1':{
    'rollno':41,
    'name':"Yash",
    'marks':85,
    'grade':None,
},
's2':{
    'rollno':42,
    'name':"Nimesh",
    'marks':90,
    'grade':None,
},
's3':{
    'rollno':43,
    'name':"Aryan",
    'marks':75,
    'grade':None,
},
's4':{
    'rollno':44,
    'name':"Sidharth",
    'marks':80,
    'grade':None,
},
's5':{
    'rollno':45,
    'name':"Isha",
    'marks':85,
    'grade':None,
}

}

for key in student:
    if student[key]['marks']>=90 and student[key]['marks']<=100:
        student[key]['grade'] = 'A'
        print(student[key]['grade'])

    elif student[key]['marks']>=80 and student[key]['marks']<90:
        student[key]['grade'] = 'B'
        print(student[key]['grade'])
    elif student[key]['marks']>=70 and student[key]['marks']<80:
        student[key]['grade'] = 'C'
        print(student[key]['grade'])
    elif student[key]['marks']>=60 and student[key]['marks']<70:
        student[key]['grade'] = 'D'
        print(student[key]['grade'])
    elif student[key]['marks']>=40 and student[key]['marks']<60:
        student[key]['grade'] = 'E'
        print(student[key]['grade'])
    else:
        print("Fail")

print("Student Information")
print(student)

