def all_eq(s):
    max_len = max(len(k)for k in s)
    res = []

    for i in s:
        res.append(i + "_" * (max_len - len(i)))
    return res

print(all_eq(["hi", "hello", "hey"]))