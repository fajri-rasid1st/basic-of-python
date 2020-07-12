import datetime

time_format = "%a %d %b %Y %H:%M:%S %z"

for i in range(int(input())):
    delta = datetime.datetime.strptime(
        input(), time_format
    ) - datetime.datetime.strptime(input(), time_format)
    print(abs(int(delta.total_seconds())))
