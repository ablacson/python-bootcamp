student_names = ("Juan", "Maria", "Joseph")
student_scores = (70, 90, 81)

# TODO: Print the student scores and names in the following format
""" 
    Student Records:
    Student: Juan scored 70 in the exam.
    Student: Maria scored 90 in the exam.
    Student: Joseph scored 81 in the exam.
"""

for name, score in zip(student_names, student_scores):
    print(f"Student: {name} scored {score} in the exam")

print(f"Student: name scored score in the exam")

# Part that goes names the highest scorer
highest_score = max(student_scores)
index = student_scores.index(highest_score)
name = student_names[index]
print(f"Top Scorer: {name} with {highest_score}")