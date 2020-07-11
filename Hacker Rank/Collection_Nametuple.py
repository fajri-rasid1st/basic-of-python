# Collections.Nametuple()

total_student = int(input())
columns_order = input().split()
total_marks = 0

for item in range(total_student):
    student_status = input().split()
    x = list(zip(columns_order, student_status))
    total_marks += int(x[columns_order.index("MARKS")][1])

print("%.2f" % (total_marks / total_student))
