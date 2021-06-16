student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

def score_to_grade(dict, new_dict, key):
    if dict[key] > 90:
        new_dict[key] = 'Outstanding'
    elif dict[key] > 80:
        new_dict[key] = 'Exceeds Expectations'
    elif dict[key] > 70:
        new_dict[key] = 'Acceptable'
    else:
        new_dict[key] = 'Fail'

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score_to_grade(student_scores, student_grades, student)   

# 🚨 Don't change the code below 👇
print(student_grades)





