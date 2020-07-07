# Find Angle MBC

import math

a, c = int(input()), int(input())

b = math.hypot(a, c) / 2

d = math.sqrt((math.pow(a, 2) / 2) + (math.pow(c, 2) / 2) - (math.pow(math.hypot(a, c), 2) / 4))

teta_result = (math.pow(d, 2) + math.pow(a, 2) - math.pow(b, 2)) / (2 * d * a)

print(round(90 - math.degrees(math.acos(teta_result))), chr(176), sep="")
