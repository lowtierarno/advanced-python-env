def all_eq(s):
    max_len = max(len(s) for s in s)
    res = []

    for i in s:
        res.append(s + "_" * (max_len - len(i)))
    return res