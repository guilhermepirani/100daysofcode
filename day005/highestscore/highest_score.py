'''You are going to write a program that calculates the highest score from a List of scores.
You are not allowed to use the max or min functions.'''

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
h_score = 0

# Updates h_score each time it parses a higher value
for score in student_scores:
    if score > h_score:
        h_score = score

print(f'The highest score in the class is: {h_score}')