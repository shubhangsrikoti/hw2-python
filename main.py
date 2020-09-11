#Author: Shubhang Srikoti svs6959@psu.edu


A = 4.0
Aminus = 3.67
Bplus = 3.33
B = 3.0
Bminus = 2.67
Cplus = 2.33
C = 2.0
D = 1.0
Fandbelow = 0.0



courseletter = input("Enter your course 1 letter grade: ")  
course1credit = float(input("Enter your course 1 credit: "))

gradepoint1 = 0
gradepoint2 = 0
gradepoint3 = 0

if courseletter == "A":
  print("Grade point for course 1 is:",A)
  gradepoint1 =+ A
elif courseletter == "A-":
  print("Grade point for course 1 is:",Aminus)
  gradepoint1 =+ Aminus
elif courseletter == "B+": 
  print("Grade point for course 1 is:",Bplus)
  gradepoint1 =+ Bplus
elif courseletter == "B":
  print("Grade point for course 1 is:",B)
  gradepoint1 =+ B
elif courseletter == "B-":
  print("Grade point for course 1 is:",Bminus)
  gradepoint1 =+ Bminus
elif courseletter == "C+":
  print("Grade point for course 1 is:",Cplus)
  gradepoint1 =+ Cplus
elif courseletter == "C":
  print("Grade point for course 1 is:",C)
  gradepoint1 =+ C
elif courseletter == "D":
  print("Grade point for course 1 is:",D)
  gradepoint1 =+ D
else:
  print("Grade point for course 1 is:",Fandbelow)
  gradepoint1 =+ Fandbelow

courseletter = input("Enter your course 2 letter grade: ")
course2credit = float(input("Enter your course 2 credit: "))
if courseletter == "A":
  print("Grade point for course 2 is:", A)
  gradepoint2 =+ A
elif courseletter == "A-":
  print("Grade point for course 2 is:",Aminus)
  gradepoint2 =+ Aminus
elif courseletter == "B+": 
  print("Grade point for course 2 is:",Bplus)
  gradepoint2 =+ Bplus
elif courseletter == "B":
  print("Grade point for course 2 is:",B)
  gradepoint2 =+ B
elif courseletter == "B-":
  print("Grade point for course 2 is:",Bminus)
  gradepoint2 =+ Bminus
elif courseletter == "C+":
  print("Grade point for course 2 is:",Cplus)
  gradepoint2 =+ Cplus
elif courseletter == "C" or courseletter == "c":
  print("Grade point for course 2 is:",C)
  gradepoint2 =+ C
elif courseletter == "D":
  print("Grade point for course 2 is:",D)
  gradepoint2 =+ D
else:
  print("Grade point for course 2 is:",Fandbelow)
  gradepoint2 =+ Fandbelow

courseletter = input("Enter your course 3 letter grade: ")
course3credit = float(input("Enter your course 3 credit: "))

if courseletter == "A":
  print("Grade point for course 3 is:",A)
  gradepoint3 =+ A
elif courseletter == "A-":
  print("Grade point for course 3 is:",Aminus)
  gradepoint3 =+ Aminus
elif courseletter == "B+": 
  print("Grade point for course 3 is:",Bplus)
  gradepoint3 =+ Bplus
elif courseletter == "B":
  print("Grade point in course 3 is:",B)
  gradepoint3 =+ B
elif courseletter == "B-":
  print("Grade point for course 3 is:",Bminus)
  gradepoint3 =+ Bminus
elif courseletter == "C+":
  print("Grade point for course 3 is:",Cplus)
  gradepoint3 =+ Cplus
elif courseletter == "C":
  print("Grade point for course 3 is:",C)
  gradepoint3 =+ C
elif courseletter == "D":
  print("Grade point for course 3 is:",D)
  gradepoint3 =+ D
else:
  print("Grade point for course 3 is:",Fandbelow)
  gradepoint3 =+ Fandbelow
  
  gpa = (gradepoint1 * course1credit + gradepoint2 * course2credit + gradepoint3 * course3credit) / (course1credit + course2credit + course3credit)
  print("Your GPA is:",gpa) 