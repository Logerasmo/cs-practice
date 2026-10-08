def parse_record(line = str):
    a = dict()
    l = line.split(";")
    if len(l) != 3:
        raise ValueError("Полей должно быть ровно 3")
    if l[0] == "" or l[2] == "":
        raise ValueError("Город или дата не могут быть пустыми")
        try:
            temp = float(l[1])
        except ValueError:
            raise ValueError("Температура должна быть числом")
    a["city"] = l[0]
    a["temperature"] = float(l[1])
    a["date"] = l[2]
    return a

def read_valid(lines = []):
    a = []
    for s in lines:
        try:
            a.append(parse_record(s))
        except ValueError:
            pass
    return a

def average_by_city(records):
    avg = dict()
    count = dict()
    for r in records:
        city = r["city"]
        if city in avg:
            avg[city] = avg[city] + r["temperature"]
            count[city] = count[city] + 1
        else:
            avg[city] = r["temperature"]
            count[city] = 1
    for k in avg:
        avg[k] = avg[k] / count[k]
    return avg

def warmest_city(records):
    avg_dict = records
    lst = []
    maxx = -99999999999
    for k in avg_dict:
        if avg_dict[k] > maxx:
            maxx = avg_dict[k]
            lst = [k]
        elif avg_dict[k] == maxx:
            lst.append(k)
    return sorted(lst)[0]
print(read_valid("Азов24.5;2026-07-01\nАзов;25.5;2026-07-02\nТаганрог;30;2026-07-01\njkvfjk".split("\n")))
