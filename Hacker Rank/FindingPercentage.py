# Finding the percentage

if __name__ == "__main__":

    n = int(input())
    student_marks = {}

    for i in range(n):

        name, *line = input().split(" ")
        scores = list(map(float, line))
        student_marks.__setitem__(name, scores)

    query_name = input()

    result = 0
    for i in student_marks.get(query_name):
        result += i

    print("%.02f" % float(result / 3))
