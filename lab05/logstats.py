levels = ["DEBUG", "INFO", "WARNING", "ERROR"]

def parse_event(line):
    l = line.strip().split(maxsplit = 2)
    if len(l) <3 or l[1] not in levels:
        raise ValueError(f"Ошибка в {line}")
    return {"time": l[0], "level": l[1], "message": l[2]}
def count_levels(lines):
    s = {}
    for line in lines:
        level = ""
        try:
            l = parse_event(line)
            level = l["level"]
        except ValueError:
            level = "BROKEN"
        s[level] = s.get(level, 0) + 1
    return s

def top_errors(lines, n):
    s = {}
    for line in lines:
        try:
            l = parse_event(line)
        except ValueError:
            continue
        if l["level"] == "ERROR":
            s[l["message"]] = s.get(l["message"], 0) + 1
    s = sorted(s.items(), key=lambda x: (-x[1], x[0]))
    return [[m, c] for m, c in s[:n]]

def format_report(counts, errors):
    t = "Отчёт по журналу\n\n"
    for level in sorted(counts):
        t += f"{level}: {counts[level]}\n"
    t += "\nЧастые ошибки:\n"
    for m, c in errors:
        t += f"- {m.strip()} — {c}\n"
    return t
