## Author: Shubhang Srikoti svs6959@psu.edu



def getGradePoint(courseletter):
  if courseletter == "A":
    return 4.0
  elif courseletter == "A-":
    return 3.67
  elif courseletter == "B+": 
    return 3.33
  elif courseletter == "B":
    return 3.0
  elif courseletter == "B-":
    return 2.67
  elif courseletter == "C+":
    return 2.33
  elif courseletter == "C":
    return 2.0
  elif courseletter == "D":
    return 1.0
  else:
    return 0.0

def run():
  courseletter1 = input("Enter your course 1 letter grade: ")
  course1credit = float(input("Enter your course 1 credit: "))
  gradepoint1 = getGradePoint(courseletter1)
  print (f"Grade point for course 1 is: {getGradePoint(courseletter1)}")
  courseletter2 = input("Enter your course 2 letter grade: ")
  course2credit = float(input("Enter your course 2 credit: "))
  gradepoint2 = getGradePoint(courseletter2)
  print (f"Grade point for course 2 is: {getGradePoint(courseletter2)}")
  courseletter3 = input("Enter your course 3 letter grade: ")
  course3credit = float(input("Enter your course 3 credit: "))
  gradepoint3 = getGradePoint(courseletter3)
  print (f"Grade point for course 3 is: {getGradePoint(courseletter3)}")
  

  gpa = (gradepoint1 * course1credit + gradepoint2 * course2credit + gradepoint3 * course3credit) / (course1credit + course2credit + course3credit)

  print("Your GPA is:",gpa) 

if __name__ == "__main__":
  run ()