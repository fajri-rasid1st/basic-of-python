# Validating Phone Number
import re

for i in range(int(input())):

    matches = re.search(r"^(7|8|9)\d{9}$", input())

    if matches == None:
        print("NO")
    else:
        print("YES")

