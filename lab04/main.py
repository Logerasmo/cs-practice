import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
total = {}
count = {}

records = read_valid(lines)
print(len(records))
print(len(records) - len(lines))
avg = average_by_city(records)
print(avg[warmest_city(avg)])
gr
