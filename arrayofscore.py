import sys

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
average = total / len(scores)

print("scores:", scores)
print("sum:",total)
print("average:",average)

maximum = max(scores)
minimum = min(scores)

print("maximum:", maximum)
print("minimum:", minimum)