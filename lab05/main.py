import os

from logstats import count_levels, top_errors, format_report

mainpath = os.path.dirname(os.path.abspath(__file__))
name = input().strip()
path = os.path.join(mainpath, name)

with open(path, encoding="utf-8") as log:
    counts = count_levels(log)
with open(path, encoding="utf-8") as log:
    errors = top_errors(log, 3)

print(sum(counts.values()))
print(counts.get("ERROR", 0))
print(counts.get("BROKEN", 0))

report_path = os.path.join(mainpath, "report.txt")
with open(report_path, "w", encoding="utf-8", newline="\n") as out:
    out.write(format_report(counts, errors))