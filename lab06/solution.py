def count_by_extension(paths):
    result = {}
    for path in paths:
        name = path.split("/")[-1]
        if "." in name:
            ext = name.rsplit(".", 1)[-1].lower()
        else:
            ext = ""
        result[ext] = result.get(ext, 0) + 1
    return result


def deepest_path(paths):
    if not paths:
        return ""
    max_depth = -1
    candidates = []
    for p in paths:
        depth = p.count("/")
        if depth > max_depth:
            max_depth = depth
            candidates = [p]
        elif depth == max_depth:
            candidates.append(p)
    return min(candidates)

def human_size(n_bytes):
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = n_bytes
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    if unit_index == 0:
        return f"{int(size)} {units[unit_index]}"
    return f"{size:.1f} {units[unit_index]}"
