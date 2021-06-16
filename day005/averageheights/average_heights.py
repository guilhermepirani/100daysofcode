'''You are going to write a program that calculates the average student height from a List of heights.
Important You should not use the sum() or len() functions in your answer.
You should try to replicate their functionality using what you have learnt about for loops.'''
# print(round(sum(student_heights) / len(student_heights)))

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
heights_sum = 0
n_students = 0

# For each student adds his height to sum and 1 to number of students.
for height in student_heights:
    heights_sum += height
    n_students += 1

print(round(heights_sum / n_students))