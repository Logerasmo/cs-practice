def toType(text):
    try:
        text = float(text)
    except:
        try:
            text = int(text)
        except:
            if text.lower() == "true" or text.lower() == "yes":
                return True
            elif text.lower() == "false" or text.lower() == "no":
                return False
    return text
def parseLineYaml(text):
    return [toType(i.strip()) for i in text.split(":")]
def csv_to_records(text):
    lines = text.splitlines()
    headers = [h.strip() for h in lines[0].split(",")]
    result = []
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        result.append(dict(zip(headers, values)))
    return result
def parse_settings(lines):
    d = dict()
    isCol = False
    mCols = []
    colName = None
    for line in lines:
        line = line.split("#", 1)[0].strip()
        if not line:
            continue
        if isCol:
            if line.startswith("-"):
                mCols.append(line[2:])
            else:
                d[colName] = mCols
                mCols = []
                isCol = False
                colName = None
            continue
        if line.endswith(":") and ":" not in line[:-1]:
            isCol = True
            colName = line[:-1].strip()
            continue

        parsed = parseLineYaml(line)
        d[parsed[0]] = parsed[1]
    if len(mCols) != 0:
        d[colName] = mCols
    return d
def records_to_json(records):
    def dump(value, indent):
        pad = "  " * indent
        inner_pad = "  " * (indent + 1)
        if isinstance(value, dict):
            if not value:
                return "{}"
            items = []
            for k in sorted(value.keys()):
                items.append(f'{inner_pad}{escape(k)}: {dump(value[k], indent + 1)}')
            return "{\n" + ",\n".join(items) + "\n" + pad + "}"
        if isinstance(value, list):
            if not value:
                return "[]"
            items = [f'{inner_pad}{dump(v, indent + 1)}' for v in value]
            return "[\n" + ",\n".join(items) + "\n" + pad + "]"
        if isinstance(value, str):
            return escape(value)
        if value is True:
            return "true"
        if value is False:
            return "false"
        if value is None:
            return "null"
        if isinstance(value, (int, float)):
            return repr(value)
        raise TypeError(f"Unsupported type: {type(value).__name__}")

    def escape(s):
        out = ['"']
        for ch in s:
            if ch == '"':
                out.append('\\"')
            elif ch == "\\":
                out.append("\\\\")
            elif ch == "\n":
                out.append("\\n")
            elif ch == "\r":
                out.append("\\r")
            elif ch == "\t":
                out.append("\\t")
            elif ord(ch) < 0x20:
                out.append("\\u%04x" % ord(ch))
            else:
                out.append(ch)
        out.append('"')
        return "".join(out)

    return dump(records, 0)
# def merge_by_key(rows, extra, key):
#     result = []
#     for row in rows:
#         merged = dict(row)
#         row_key = row.get(key)
#         if row_key in extra:
#             for k, v in extra[row_key].items():
#                 if k not in merged:
#                     merged[k] = v
#         result.append(merged)
#     return result
def merge_by_key(rows, extra, key):
    result = []
    for row in rows:
        row_key = row.get(key)
        merged = dict(extra.get(row_key, {}))
        merged.update(row)
        result.append(merged)
    return result
