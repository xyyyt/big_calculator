def check_list_has_duplicates(l):
    if not l:
        return False

    s = set()

    for v in l:
        if v in s:
            return True

        s.add(v)

    return False
